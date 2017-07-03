import os
try:
    import ConfigParser as configparser
except ImportError:
    import configparser
from yaml import load
from onionrouter.olib import find_file, find_files_with_suffix
from onionrouter.custom_exceptions import (ConfigIntegrityError,
                                           ConfigNotFoundError)


class ConfigIntegrityChecker(object):
    def __init__(self, ref_config, other_config):
        self._ref_reader = config_reader(ref_config)
        self._oth_reader = config_reader(other_config)
        self.ref_config = ref_config
        self.other_config = other_config

    def _verify_sections(self):
        if set(self._ref_reader.sections()).difference(
                set(self._oth_reader.sections())):
            raise RuntimeError

    def _verify_options(self):
        for section in self._ref_reader.sections():
            if set(self._ref_reader.options(section)).difference(
                    set(self._oth_reader.options(section))):
                raise RuntimeError

    def verify(self):
        try:
            self._verify_sections()
            self._verify_options()
        except RuntimeError:
            raise ConfigIntegrityError(
                "{loc} does not match the reference config file {ref}\n"
                "Is your local config up to date?".format(
                    loc=self.other_config, ref=self.ref_config))


def config_reader(conf_path):
    """
    Reads a conf file and returns the onfigParser object
    """
    config = configparser.ConfigParser()
    config.read(conf_path)
    return config


def get_conffile(conf_path, prefix='', suffix=".ini"):
    """
    Finds conf file in `conf_path`
    If `conf_path` is file, returns `conf_path`
    Else it searches to find a file with `prefix``suffix` format
    """
    if os.path.isfile(conf_path):
        return conf_path

    found_file = find_file(conf_path, "{0}{1}".format(prefix, suffix))
    if not found_file:
        raise ConfigNotFoundError('No configuration file found in {0}'
                                  .format(conf_path))
    return found_file


def yaml_loader(yaml_path):
    """
    Yields yaml files
    Supports folder lookup
    :param yaml_path: path pointing to a yaml file or a dir with yaml files
    :return: yields open file
    """
    if not os.path.exists(yaml_path):
        return

    if os.path.isdir(yaml_path):
        all_files = sorted(find_files_with_suffix(yaml_path, "yml"))
    else:
        all_files = [yaml_path]

    for filename in all_files:
        with open(filename, 'r') as yaml_file:
            yield yaml_file


def load_yamls(yaml_path):
    """
    Returns a dict with mappings defined in yaml file(s)
    :param yaml_path: path pointing to a yaml file or a dir with yaml files
    :rtype: dict
    """
    yaml_mapping = dict()
    for f in yaml_loader(yaml_path):
        yaml_mapping.update(load(f))
    return yaml_mapping
