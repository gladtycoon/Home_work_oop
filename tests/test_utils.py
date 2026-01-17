import json

import pytest

from src.utils import read_json, create_objects_from_json


def test_read_json_valid_file(tmp_path):
    """Проверяет чтение корректного JSON-файла."""
    # 1. Подготовка: Создаём временный файл с данными
    test_data = [{"name": "product1", "price": 100}, {"name": "product2", "price": 200}]
    file_path = tmp_path / "test_data.json"
    file_path.write_text(json.dumps(test_data), encoding="UTF-8")

    # 2. Действие: Читаем файл через тестируемую функцию
    result = read_json(str(file_path))

    # 3. Проверка: Данные соответствуют ожиданиям
    assert result == test_data
    assert len(result) == 2
    assert result[0]["name"] == "product1"
    assert result[0]["price"] == 100
    assert result[1]["name"] == "product2"
    assert result[1]["price"] == 200


def test_read_json_file_not_found():
    """Проверяет реакцию на отсутствие файла."""
    with pytest.raises(FileNotFoundError):
        read_json("non_existent_file.json")


def test_create_objects_multiple_categories():
    """Проверяет создание объектов для нескольких категорий."""
    json_data = [
        {"name": "cat1", "description": "description_cat1", "products": [{"name": "prod1", "description": "description_prod1", "price": 100.0, "quantity": 1}]},
        {"name": "cat2", "description": "description_cat2", "products": [{"name": "prod2", "description": "description_prod2", "price": 200.0, "quantity": 2}]}
    ]
    categories = create_objects_from_json(json_data)
    assert len(categories) == 2
    assert categories[0].name == "cat1"
    assert categories[1].name == "cat2"