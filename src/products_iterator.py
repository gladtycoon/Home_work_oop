# Вспомогательный класс для перебора товаров одной категории
class ProductIterator:
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_in_list):
            type_of_product = self.category.products_in_list[self.index]
            self.index += 1
            return type_of_product
        else:
            raise StopIteration
