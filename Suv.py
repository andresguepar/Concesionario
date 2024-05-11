from abc import ABC, abstractmethod
class Suv(ABC):
    @abstractmethod
    def getDescription(self):
        pass