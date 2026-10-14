class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, app_name, delivery_fee):
        if not hasattr(self, "_initialized"):
            self.app_name = app_name
            self.delivery_fee = delivery_fee
            self._initialized = True


restaurant_config = AppConfig("Zomato", 40)
order_config = AppConfig("Swiggy", 60)
payment_config = AppConfig("Other", 100)

print(restaurant_config is order_config)
print(order_config is payment_config)

print(restaurant_config.app_name)
print(restaurant_config.delivery_fee)
print(payment_config.delivery_fee)