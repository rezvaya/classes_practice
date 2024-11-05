'''
1. Как метод show_info в классе Car использует метод show_info из класса Vehicle?
2. Почему используется super() для вызова метода родителя?
3. Что произойдет, если убрать super().show_info() из метода show_info в классе Car?
'''

# Базовый класс Транспортное средство
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        return f"{self.brand} can go up to {self.speed} km/h"

# Дочерний класс Автомобиль
class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        # Вызов конструктора родительского класса
        super().__init__(brand, speed)
        self.num_doors = num_doors

    def show_info(self):
        parent_info = super().show_info()
        return f"{parent_info} and has {self.num_doors} doors"

# Создаем объекты классов
vehicle = Vehicle("Generic Vehicle", 100)
car = Car("Toyota", 150, 4)

# Вывод информации
print(vehicle.show_info())
print(car.show_info())
