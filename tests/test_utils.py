from src.created_classes import Category

def test_product_init(class_product):
    assert class_product.name == "name"
    assert class_product.description == "description"
    assert class_product.price == "price"
    assert class_product.quantity == "quantity"


def test_category_init(class_category):
    assert class_category.name == "name"
    assert class_category.description == "description"
    assert class_category.products == []

    assert Category.category_count == 1
    assert Category.product_count == 0
