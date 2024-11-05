'''
1. Исправьте код так, чтобы ElectricCar корректно вызывал конструктор Vehicle для инициализации brand и speed.
2. Проверьте работу метода show_info после исправления.
(?) Зачем нужно вызывать конструктор родительского класса в дочернем классе?
'''

# Базовый класс Транспортное средство
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        return f"{self.brand} can go up to {self.speed} km/h"

# Дочерний класс Электромобиль
class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery_capacity):
        self.battery_capacity = battery_capacity  # Инициализация аккумулятора

    def show_info(self):
        return f"{self.brand} with a battery capacity of {self.battery_capacity} kWh can go up to {self.speed} km/h"

# Создаем объект класса ElectricCar
tesla = ElectricCar("Tesla", 200, 100)
print(tesla.show_info())
