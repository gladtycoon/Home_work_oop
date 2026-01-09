import pytest

from src.created_classes import Product, Category

@pytest.fixture
def class_product():
    return Product(
        name="name",
        description="description",
        price="price",
        quantity="quantity"
    )

@pytest.fixture
def class_category():
    return Category(
        name="name",
        description="description",
        products=[]
    )