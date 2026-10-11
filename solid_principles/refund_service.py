from abc import  ABC, abstractmethod

class Refundable(ABC):
    @abstractmethod
    def refund(self):
        pass