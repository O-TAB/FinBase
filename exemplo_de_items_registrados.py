from enum import Enum


class Category(str, Enum):
    COXINHA = "Coxinha"
    EMPADA = "Empada"


class BaseItem:
    baseprice_map: dict = {
        Category.COXINHA: 4,
        Category.EMPADA: 5,
    }  # pode vim do banco de dados

    def __init__(self, category, expecific_price=None):
        self.category = category
        self.base_cost = (
            self.baseprice_map[self.category]
            if expecific_price is None
            else expecific_price
        )


class Item(BaseItem):
    def __init__(self, category, name, expecific_price=None):
        super().__init__(category, expecific_price)
        self.name = name


items = [Item("Coxinha", "Coxinha de frango"), Item("Coxinha", "Coxinha invocada", 10)]
for i in items:
    print(f"{i.name}, {i.base_cost}, {i.category}")
