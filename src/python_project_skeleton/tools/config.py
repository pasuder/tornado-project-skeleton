import ConfigParser
import sys

__author__ = 'paoolo'


class Config(object):
    def __init__(self, *args):
        self.__config = ConfigParser.ConfigParser()
        self.add_config_ini(*args)

    def __getattr__(self, name):
        # noinspection PyBroadException
        try:
            return self.__config.get('default', name)
        except Exception as n_exp:
            print('Cannot found value for %s in config: %s\n' % (name, n_exp))
            return None

    def set_attr(self, key, value):
        # noinspection PyBroadException
        try:
            self.__config.set('default', key, str(value))
        except Exception as n_exp:
            print('Cannot set value %s for %s to config: %s\n' % (value, key, n_exp))

    def add_config_ini(self, *args):
        map(lambda config_file_path: self.__config.read(config_file_path), args)


sys.modules[__name__] = Config()


def add_config_ini(*args):
    sys.modules[__name__].add_config_ini(*args)


def set_attr(*args):
    sys.modules[__name__].set_attr(*args)
