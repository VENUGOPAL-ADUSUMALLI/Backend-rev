from abc import  ABC, abstractmethod

class OrderRepository(ABC):

    @abstractmethod
    def save(self):
        pass