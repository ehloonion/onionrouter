from abc import abstractmethod, ABCMeta
from dns import exception as dnsexception
from onionrouter.config_handlers import load_yamls


class PostfixRerouter(object):
    __metaclass__ = ABCMeta

    def __init__(self, config):
        self.config = config

    @property
    def reroute_service(self):
        return self.config.get("REROUTE", "onion_transport")

    @abstractmethod
    def reroute(self, answers):
        return tuple("200 {rservice}:[{ans}]".format(
            rservice=self.reroute_service, ans=x) for x in answers)


class LazyPostfixRerouter(PostfixRerouter):
    def __init__(self, config, yaml_path):
        super(LazyPostfixRerouter, self).__init__(config)
        self.mappings_path = yaml_path
        self.static_mappings = dict()

    def _setup_static_mappings(self):
        for (key, vals) in load_yamls(self.mappings_path).items():
            self.static_mappings.update({x.upper(): key for x in vals})

    def _lazy(self, domain):
        mapping = self.static_mappings.get(domain.upper())
        return tuple([mapping]) if mapping else tuple()

    def reroute(self, domain):
        if not self.static_mappings:
            self._setup_static_mappings()
        return super(LazyPostfixRerouter, self).reroute(self._lazy(domain))


class OnionPostfixRerouter(PostfixRerouter):
    def __init__(self, config, onion_resolver):
        super(OnionPostfixRerouter, self).__init__(config)
        self.onion_resolver = onion_resolver

    def reroute(self, domain):
        try:
            return super(OnionPostfixRerouter, self).reroute(
                self.onion_resolver.lookup(domain))
        except dnsexception.DNSException as err:
            return tuple(("500 {0}".format(str(err) or "Not found"),))
