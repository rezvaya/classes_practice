'''
1. Какую информацию предоставляет isinstance?
2. Как issubclass помогает проверить иерархию классов?
3. Что произойдет, если проверить isinstance(device, Laptop)?
'''

# Базовый класс Электронное устройство
class ElectronicDevice:
    def __init__(self, brand):
        self.brand = brand

# Дочерний класс Смартфон
class Smartphone(ElectronicDevice):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

# Дочерний класс Ноутбук
class Laptop(ElectronicDevice):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

# Создаем объекты
device = ElectronicDevice("Generic Brand")
phone = Smartphone("Apple", "iPhone 13")
laptop = Laptop("Dell", "XPS 15")

# Проверка типов
print(isinstance(phone, Smartphone))   # True
print(isinstance(phone, ElectronicDevice))  # True
print(isinstance(laptop, ElectronicDevice))  # True
print(isinstance(device, Smartphone))  # False

# Проверка подклассов
print(issubclass(Smartphone, ElectronicDevice))  # True
print(issubclass(Laptop, ElectronicDevice))  # True
print(issubclass(ElectronicDevice, Laptop))  # False
