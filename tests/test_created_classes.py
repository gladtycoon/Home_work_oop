from src.created_classes import Category, Product


def test_product_init(class_product):
    assert class_product.name == "name"
    assert class_product.description == "description"
    assert class_product.price == "price"
    assert class_product.quantity == "quantity"


def test_category_init(class_category):
    assert class_category.name == "name"
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


def test_price_setter(class_product):
    class_product.price = 180000.0
    assert class_product.price == 180000.0

    class_product.price = 0.0
    assert class_product.price == 180000.0  # Цена не изменилась!
    print(f"Цена после попытки установить 0.0: {class_product.price}")

    class_product.price = -100.0
    assert class_product.price == 180000.0  # Цена не изменилась!
    print(f"Цена после попытки установить 0.0: {class_product.price}")