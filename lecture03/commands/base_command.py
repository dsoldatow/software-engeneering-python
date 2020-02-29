from abc import ABC, abstractmethod


class BaseCommand(ABC):
    @staticmethod
    @abstractmethod
    def info(): pass

    @staticmethod
    @abstractmethod
    def run( **kwargs): pass
