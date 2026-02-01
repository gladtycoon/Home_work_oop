from abc import ABC, abstractmethod


# Создание базового класса
class BaseProduct(ABC):


# Описание общей функциональности каждого продукта - создания нового продукта
    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
