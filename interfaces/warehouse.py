from abc import ABC, abstractmethod


class WarehouseInterface(ABC):
    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def remove_product(self, product):
        pass

    @abstractmethod
    def get_all_products(self):
        pass
