'''
1. Какой метод вызывается для объектов dog и cat, и почему он отличается от метода в Animal?
2. Что произойдет, если удалить метод speak из класса Dog?
'''


# Базовый класс Животное
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound"

# Дочерний класс Собака
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Дочерний класс Кошка
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Создаем объекты классов
animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Выводим звуки животных
print(animal.name, "says:", animal.speak())
print(dog.name, "says:", dog.speak())
print(cat.name, "says:", cat.speak())
