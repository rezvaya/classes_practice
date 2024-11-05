'''
1. Допишите метод flight_time, чтобы он возвращал время, необходимое для преодоления заданного расстояния (в часах).
2. Убедитесь, что метод работает корректно, создав объект и вызвав метод с тестовым расстоянием.
3. Используйте метод super() в методе __init__ для вызова конструктора родительского класса.
'''

# Базовый класс Животное
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic animal sound"

# Дочерний класс Птица
class Bird(Animal):
    def __init__(self, name, wing_span, speed):
        super().__init__(name)
        self.wing_span = wing_span
        self.speed = speed

    def sound(self):
        return "Chirp!"

    # Метод для расчета времени полета (добавить)
    def flight_time(self, distance):
        # Использовать скорость для расчета времени (время = расстояние / скорость)
        pass

# Создаем объект класса Bird
eagle = Bird("Eagle", 2.3, 50)

# Попытка вызвать метод для расчета времени полета на 100 км
print(eagle.flight_time(100))
