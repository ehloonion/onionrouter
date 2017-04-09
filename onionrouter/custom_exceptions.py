class ConfigError(Exception):
    pass


class ConfigNotFoundError(ConfigError):
    pass


class ConfigIntegrityError(ConfigError):
    pass
