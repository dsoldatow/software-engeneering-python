from abc import ABC, abstractmethod


class BaseObject(ABC):
    @staticmethod
    @abstractmethod
    def description(): pass

    @staticmethod
    @abstractmethod
    def short_description(): pass
