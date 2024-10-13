from abc import ABC

from interfaces.warehouse import WarehouseInterface
from interfaces.product import ProductInterface


class Warehouse(WarehouseInterface, ABC):

    def __init__(self, city, owner, capacity):
        self.city = city
        self.owner = owner
        self.capacity = capacity
        self.products = []

    def get_all_products(self):
        return [p.get_name() for p in self.products]

    def add_product(self, product: ProductInterface):
        self.products.append(product)

    def remove_product(self, product: ProductInterface):
        self.products.remove(product)
