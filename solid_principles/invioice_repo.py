from abc import  ABC, abstractmethod

class InvoiceRepo(ABC):

    @abstractmethod
    def generate_invoice(self):
        pass