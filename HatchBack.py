from abc import ABC, abstractmethod
class HatchBack(ABC):
    @abstractmethod
    def getDescription(self):
        pass