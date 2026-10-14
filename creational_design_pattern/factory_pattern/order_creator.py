from abc import ABC, abstractmethod
from creational_design_pattern.factory_pattern.abstract_factory import ItemPrepare


class OrderCreator(ABC):

    @abstractmethod
    def create_order(self) -> ItemPrepare:
        pass

    def process_order(self):
        order = self.create_order()
        return order.prepare()