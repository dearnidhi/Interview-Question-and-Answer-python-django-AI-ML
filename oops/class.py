#1. Classes and Objects:
"""Class: A class is a blueprint for creating objects.
 It defines attributes (data) and methods (functions) that the objects created from the class will have.
Object: An object is an instance of a class. It is a concrete entity based on the class definition."""
# Example of a simple class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

# Creating an instance (object) of the Dog class
my_dog = Dog(name="Buddy", age=3)

# Accessing attributes and calling methods
print(my_dog.name)
print(my_d og.age)
print(my_dog.bark())

"""
In Python, __init__ is a special method (sometimes called a "dunder" method, short for double underscore) that is used for initializing the attributes of an object when it is created.
 The full name of the method is __init__ (two underscores before and after "init")."""