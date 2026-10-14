from abc import  ABC, abstractmethod

class ItemPrepare(ABC):

    @abstractmethod
    def prepare(self):
        pass