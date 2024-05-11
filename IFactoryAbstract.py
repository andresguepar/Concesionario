from abc import ABC, abstractmethod

class IFactoryAbstract(ABC):
    @abstractmethod
    def createSedan(self):
        pass
    @abstractmethod
    def createSuv(self):
        pass
    @abstractmethod
    def createHactchback(self):
        pass