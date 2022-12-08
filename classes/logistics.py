from abc import ABC, abstractmethod

class Storage(ABC):

    def __init__(self, items:dict, capacity:int):
        self.items = items
        self.capacity = capacity


    def add(self, name_product, amount):
        self.items['name_product'] = amount
        self.capacity += amount

    def remove(self):
        pass

    def get_free_space(self):
        pass

    def get_items(self):
        pass

    def get_unique_items_count(self):
        pass


class Store:
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def add(self):
        pass

    def remove(self):
        pass

    def get_free_space(self):
        pass

    def get_items(self):
        pass

    def get_unique_items_count(self):
        pass


class Shop:
    pass


class Request:
    pass
