from creational_design_pattern.factory_pattern.food_factory import FoodOrder
from creational_design_pattern.factory_pattern.gorcery_factory import GroceryOrder
from creational_design_pattern.factory_pattern.medicine_factory import MedicineOrder


class OrderService:
    def create_order(self, order_type):
        if order_type == "food":
            return  FoodOrder().prepare()

        elif order_type == "grocery":
            return  GroceryOrder().prepare()

        elif order_type == "medicine":
            return  MedicineOrder().prepare()
        else:
            raise ValueError("Unsupported order type")


service = OrderService()

food = service.create_order("food")
grocery = service.create_order("grocery")

print(food)
print(grocery)
