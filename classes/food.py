from abc import ABC

from interfaces.product import ProductInterface


class Food(ProductInterface, ABC):

    def __init__(self, code, food_type, size, name, cost, quantity):
        self.code = code
        self.food_type = food_type
        self.size = size
        self.name = name
        self.cost = cost
        self.quantity = quantity

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name

    def get_price(self):
        return self.cost * self.quantity

    def get_quantity(self):
        return self.quantity
