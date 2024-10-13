from abc import ABC

from interfaces.product import ProductInterface


class Electronic(ProductInterface, ABC):

    def __init__(self, code, size, brand, model, price, quantity):
        self.size = size
        self.code = code
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity

    def get_code(self):
        return self.code

    def get_name(self):
        return self.brand + self.model

    def get_price(self):
        return self.price * self.quantity

    def get_quantity(self):
        return self.quantity
