from abc import ABC, abstractmethod
class Sedan(ABC):
    @abstractmethod
    def getDescription(self):
        pass