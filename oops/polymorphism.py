"""The word "polymorphism" means "many forms", and in programming it refers to
 methods/functions/operators with the same name that can be executed on many objects or classes.

"""

#Method Overriding:

""" Occurs when a subclass defines a method with the same name and signature
 (including return type and parameter types) as a method in its superclass.
 Provide specialized behavior
 eg:- Animal.talk() vs. Dog.talk()

."""
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def make_sound(animal):
    return animal.sound()

dog = Dog()
cat = Cat()

print(make_sound(dog))  # Output: Woof!
print(make_sound(cat))  # Output: Meow!


"""Occurs when a class defines multiple 
methods with the same name but different signatures.
Used to provide different functionalities based on the input received by the method.
eg:-Math.add(a, b) vs. Math.add(list)


"""

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating an instance of the Calculator class
calc = Calculator()

# Using the add method with different parameter lists
result1 = calc.add(1)
result2 = calc.add(1, 2)
result3 = calc.add(1, 2, 3)

print(result1)  # Output: 1
print(result2)  # Output: 3
print(result3)  # Output: 6

print(f"for first {result1},for second {result2},for third {result3}")