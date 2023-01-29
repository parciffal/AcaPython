import abc
from abc import ABC


class ABCList(ABC):

    @abc.abstractmethod
    def add(self):
        pass

    @abc.abstractmethod
    def pop(self):
        pass

    @abc.abstractmethod
    def search(self):
        pass
