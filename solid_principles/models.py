from babel.messages import setuptools_frontend


class Product:
    def  __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


class Order:
    def __init__(self, user, products):
        self.user = user
        self.products = products

    def calculate_total(self):
        return  sum(each.price for each in self.products)

