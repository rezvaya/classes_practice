'''
У нас есть базовый класс Person и дочерний класс Student. 
Задача — создать новый класс Teacher, который тоже наследуется от Person, но с уникальным методом.
* Например, метод teach, который возвращает строку: "Mr. Smith is teaching.".
'''

# Базовый класс Человек
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Дочерний класс Студент
class Student(Person):
    def study(self):
        return f"{self.name} is studying."

# Дочерний класс Преподаватель (добавить новый)
# Здесь нужно добавить класс Teacher, который имеет метод teach()

# Создаем объекты классов
person = Person("Alice", 30)
student = Student("Bob", 20)
# Создаем объект преподавателя и вызываем метод teach()

# Вызовы методов
print(person.introduce())
print(student.introduce())
print(student.study())
