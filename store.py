### Задача про магазины:


class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание объектов магазинов и тестирование методов
store1 = Store("Магазин А", "ул. Лесная, 5")
store2 = Store("Магазин Б", "пр. Мира, 12")
store3 = Store("Магазин В", "ш. Кольцово, 3")

# Добавление товаров
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

# Обновление цены товара
store1.update_price("apples", 0.6)

# Удаление товара
store1.remove_item("bananas")

# Получение цены товара
print(f"Цена яблок: {store1.get_price('apples')}")
