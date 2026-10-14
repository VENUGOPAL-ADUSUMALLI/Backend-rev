from creational_design_pattern.factory_pattern.abstract_factory import ItemPrepare

class MedicineOrder(ItemPrepare):
    def prepare(self):
        print("Creating medicine order")
        return {"type": "medicine", "delivery_fee": 20}
