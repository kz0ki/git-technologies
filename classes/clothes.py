from abc import ABC

from interfaces.product import ProductInterface


class Clothes(ProductInterface, ABC):

    def __init__(self, code, size, brand, model, price, quantity, is_collection):
        self.size = size
        self.code = code
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity
        self.is_collection = is_collection

    def get_code(self):
        return self.code

    def get_name(self):
        return self.brand * self.model

    def get_price(self):
        return self.price * self.quantity

    def get_quantity(self):
        return self.quantity

