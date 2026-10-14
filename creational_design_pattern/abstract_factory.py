
from abc import ABC, abstractmethod

class MainDish(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Dessert(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Biryani(MainDish):
    def prepare(self):
        print("Preparing Biryani")


class Pizza(MainDish):
    def prepare(self):
        print("Preparing Pizza")


class GulabJamun(Dessert):
    def prepare(self):
        print("Preparing Gulab Jamun")


class Tiramisu(Dessert):
    def prepare(self):
        print("Preparing Tiramisu")


class RestaurantFactory(ABC):
    @abstractmethod
    def create_main_dish(self):
        pass

    @abstractmethod
    def create_dessert(self):
        pass


class IndianRestaurantFactory(RestaurantFactory):
    def create_main_dish(self):
        return Biryani()

    def create_dessert(self):
        return GulabJamun()


class ItalianRestaurantFactory(RestaurantFactory):
    def create_main_dish(self):
        return Pizza()

    def create_dessert(self):
        return Tiramisu()


def serve_meal(factory: RestaurantFactory):
    main_dish = factory.create_main_dish()
    dessert = factory.create_dessert()

    main_dish.prepare()
    dessert.prepare()


factory = IndianRestaurantFactory()
serve_meal(factory)

print("-----")

factory = ItalianRestaurantFactory()
serve_meal(factory)
