from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


# Создание и инициализация класса Product
class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity != 0:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    # Строковое отображение в заданном виде
    def __str__(self):
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    # Геттер для доступа к приватному атрибуту
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    # Класс-метод, который принимает на вход параметры товара в словаре
    # и возвращает созданный объект класса
    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


# Создание и инициализация класса Smartphone - наследника от класса Product
class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.quantity + other.quantity
        raise TypeError


# Создание и инициализация класса LawnGrass - наследника от класса Product
class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.quantity + other.quantity
        raise TypeError


# Создание и инициализация класса Category
class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products  # создание приватного атрибута списка товаров
        self.sum_product = 0
        Category.category_count += 1
        Category.product_count += len(products)

        for product in self.__products:
            self.sum_product += product.quantity

    # Строковое отображение в заданном виде
    def __str__(self):
        return f"{self.name}, количество продуктов: {self.sum_product} шт."

    # Метод, в который нужно передавать объект класса Product
    # и уже его записывать в приватный атрибут списка товаров
    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    # Геттер, который выводит список товаров в виде строк в заданном формате
    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_in_list(self):
        return self.__products


    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
