import json
import os

from created_classes import Category, Product


def read_json(path: str) -> list[dict]:
    """Функция, которая принимает путь до json-файла,
    читает его и возвращает список словарей"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return data


def create_objects_from_json(data):
    """Функция создает объекты Category и Product из данных JSON-файла"""
    categories = []
    for category_data in data:
        products_list = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products_list.append(product)
        category = Category(
            name=category_data["name"], description=category_data["description"], products=products_list
        )
        categories.append(category)
    return categories


if __name__ == "__main__":
    raw_data = read_json("D:/SkyPro/Home_work_oop/data/products.json")
    created_objects = create_objects_from_json(raw_data)

# print("\n" + "=" * 50)
#     print("РЕЗУЛЬТАТ:")
#     print("=" * 50)
#
#     for i, category in enumerate(created_objects, 1):
#         print(f"\n{i}. КАТЕГОРИЯ: {category.name}")
#         print(f"   Описание: {category.description}")
#         print(f"   Продуктов в категории: {len(category.products)}")
#
#         for j, product in enumerate(category.products, 1):
#             print(f"   {j}. {product.name} - {product.price} руб. (осталось: {product.quantity})")
#
#         # Вывод счетчиков
#     print(f"\n Статистика системы:")
#     print(f"   Всего продуктов: {Category.product_count}")
#     print(f"   Всего категорий: {Category.category_count}")
