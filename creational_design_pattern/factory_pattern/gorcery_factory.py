from creational_design_pattern.factory_pattern.abstract_factory import ItemPrepare

class GroceryOrder(ItemPrepare):
    def prepare(self):
        print("Creating grocery order")
        return  {"type": "grocery", "delivery_fee": 25}
