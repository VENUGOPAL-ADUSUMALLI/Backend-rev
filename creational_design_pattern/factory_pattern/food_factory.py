from creational_design_pattern.factory_pattern.abstract_factory import ItemPrepare


class FoodOrder(ItemPrepare):
    def prepare(self):
        print("Creating food order")
        return {"type": "food", "delivery_fee": 40}
