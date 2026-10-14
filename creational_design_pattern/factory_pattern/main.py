
from abc import ABC, abstractmethod


# 1. PRODUCT INTERFACE
# Every order must implement prepare().
class ItemPrepare(ABC):

    @abstractmethod
    def prepare(self):
        pass


# 2. CONCRETE PRODUCTS
class FoodOrder(ItemPrepare):

    def prepare(self):
        print("Preparing food order")
        return {"type": "food", "delivery_fee": 40}


class GroceryOrder(ItemPrepare):

    def prepare(self):
        print("Preparing grocery order")
        return {"type": "grocery", "delivery_fee": 25}


class MedicineOrder(ItemPrepare):

    def prepare(self):
        print("Preparing medicine order")
        return {"type": "medicine", "delivery_fee": 20}


# 3. ABSTRACT CREATOR
class OrderCreator(ABC):

    @abstractmethod
    def create_order(self) -> ItemPrepare:
        pass

    # Common workflow shared by all creators.
    def process_order(self):
        order = self.create_order()
        return order.prepare()


# 4. CONCRETE CREATORS
class FoodOrderCreator(OrderCreator):

    def create_order(self) -> ItemPrepare:
        return FoodOrder()


class GroceryOrderCreator(OrderCreator):

    def create_order(self) -> ItemPrepare:
        return GroceryOrder()


class MedicineOrderCreator(OrderCreator):

    def create_order(self) -> ItemPrepare:
        return MedicineOrder()


# 5. CLIENT CODE
def main():
    food_creator = FoodOrderCreator()
    grocery_creator = GroceryOrderCreator()
    medicine_creator = MedicineOrderCreator()

    print(food_creator.process_order())
    print(grocery_creator.process_order())
    print(medicine_creator.process_order())


if __name__ == "__main__":
    main()
