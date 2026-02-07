import pytest

from src.created_classes import Category, Product
from tests.conftest import class_product


def test_product_init(class_product):
    assert class_product.name == "name"
    assert class_product.description == "description"
    assert class_product.price == 180000
    assert class_product.quantity == 5


def test_category_init(class_category):
    assert class_category.name == "Смартфоны"
    assert class_category.description == "description"
    assert class_category.products == ""

    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product(class_category, class_product):
    initial_count = Category.product_count
    class_category.add_product(class_product)
    assert Category.product_count == initial_count + 1


def test_products(class_category, class_product):
    assert class_category.products == ""
    class_category.add_product(class_product)
    expected = f"{class_product.name}, {class_product.price} руб. Остаток: {class_product.quantity} шт.\n"
    assert class_category.products == expected


def test_price_setter(class_category, class_product):
    assert len(class_category.products_in_list) == 0
    class_category.add_product(class_product)
    assert len(class_category.products_in_list) == 1


def test_new_product():
    created_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    created_product.name = "Samsung Galaxy S23 Ultra"
    created_product.description = "256GB, Серый цвет, 200MP камера"
    created_product.price = 180000.0
    created_product.quantity = 5


def test_price_setter_prod(class_product):
    class_product.price = 180000.0
    assert class_product.price == 180000.0

    class_product.price = 0.0
    assert class_product.price == 180000.0  # Цена не изменилась!
    print(f"Цена после попытки установить 0.0: {class_product.price}")

    class_product.price = -100.0
    assert class_product.price == 180000.0  # Цена не изменилась!
    print(f"Цена после попытки установить 0.0: {class_product.price}")


def test_product_str(product):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."


def test_category_str(class_category):
    assert str(class_category) == "Смартфоны, количество продуктов: 0 шт."


def test_smartphone_subclass_init(smartphone2):
    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"


def test_smartphone_subclass_add(smartphone2, smartphone3):
    assert smartphone2 + smartphone3 == 22


def test_smartphone_subclass_add_error(smartphone2, smartphone3):
    with pytest.raises(TypeError):
        smartphone2 + 1


def test_lawngrass_subclass_init(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_lawngrass_subclass_add(grass1, grass2):
    assert grass1 + grass2 == 35


def test_lawngrass_subclass_add_error(grass1, grass2):
    with pytest.raises(TypeError):
        grass1 + 1


def test_middle_price(category1, category_without_products):
    assert category1.middle_price() == 140333.33333333334
    assert category_without_products.middle_price() == 0