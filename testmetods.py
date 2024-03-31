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


# Создание объектов магазинов
store1 = Store("Магазин А", "ул. Лесная, 5")
store2 = Store("Магазин Б", "пр. Мира, 12")
store3 = Store("Магазин В", "ш. Кольцово, 3")

# Добавление товаров в store1
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

# Обновление цены товара в store1
store1.update_price("apples", 0.6)

# Удаление товара из store1
store1.remove_item("bananas")

# Добавление товаров в store2
store2.add_item("water", 0.25)
store2.add_item("chocolate", 1.5)

# Обновление цены товара в store2
store2.update_price("water", 0.3)

# Удаление товара из store2
store2.remove_item("chocolate")

# Добавление товаров в store3
store3.add_item("bread", 1.0)
store3.add_item("milk", 0.8)

# Обновление цены товара в store3
store3.update_price("bread", 1.1)

# Удаление товара из store3
store3.remove_item("milk")

# Вывод информации о ценах
print(f"Цена яблок: {store1.get_price('apples')}")
print(f"Цена воды: {store2.get_price('water')}")
print(f"Цена хлеба: {store3.get_price('bread')}")