# Создание и инициализация класса Product
class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

        Category.category_count += 1
        Category.product_count += len(products)

    # Метод, в который нужно передавать объект класса Product
    # и уже его записывать в приватный атрибут списка товаров
    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    # Геттер, который выводит список товаров в виде строк в заданном формате
    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @property
    def products_in_list(self):
        return self.__products
