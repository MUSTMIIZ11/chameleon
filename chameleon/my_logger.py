import logging


class Singleton(type):
    """
    The singleton
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyLogger(metaclass=Singleton):
    """
    Why we need logger as singleton?
    We rare use singleton but log, config,
    """
    def __init__(self):
        self._logger = logging.getLogger('Chameleon')

    def get_logger(self):
        return self._logger

class DBConnection(metaclass=Singleton):
    def __init__(self):
        self._connection = ...
    def get_connection(self):
        return self._connection

if __name__ == '__main__':
    logger1 = MyLogger().get_logger()
    logger2 = MyLogger().get_logger()
    assert logger1 == logger2, 'logger is not singleton!'
