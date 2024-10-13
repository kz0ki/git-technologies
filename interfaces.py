from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass

    @abstractmethod
    def get_code(self):
        pass


class WarehouseInt(ABC):
    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def remove_product(self, product):
        pass

    @abstractmethod
    def get_all_products(self):
        pass
