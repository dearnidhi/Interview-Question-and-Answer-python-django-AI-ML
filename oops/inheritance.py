#1. Single Inheritance:
"""In single inheritance, a class inherits from only one base class.

"""
class Animal:
    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def bark(self):
        return "Woof"

# Usage
dog = Dog()
print(dog.speak())  # Output: Generic animal sound
print(dog.bark())   # Output: Woof

#2. Multiple Inheritance:
"""In multiple inheritance, a class can inherit from more than one base class.

"""
class swimmer:
    def swim(self):
        return "swwing kr rahe h"
class flyer:
    def fly(self):        
        return "we are flying"
class duck(swimmer,flyer):
    def quack(self):
        return "quack"

Duck  = duck()
print(Duck.swim())   
print(Duck.fly())      
print(Duck.quack())  

#3. Multi-Level Inheritance:
"""in multi-level inheritance, a class inherits from another class, which, in turn, inherits from a third class."""
class vehicle:
    def start(self):
        return "start vehicle"
class car(vehicle): 
    def drive(self):
        return "car is starting"
class electriccar(car):
     def charge(self):
         return "e car is charging"
E_car= electriccar()
print(E_car.start())   
print(E_car.drive())       
print(E_car.charge())       

#4. Hierarchical Inheritance:
"""In hierarchical inheritance, multiple classes inherit from a single base class.

"""
class shape:
    def area(self):
        return "cal area"
class circle(shape):
    def cal_area(self,r):
        return 3.14*r*r 
class sqr(shape):
    def cal_area(self,s):  
        return s*s
circle=circle()
sqr=sqr() 
print(circle.area())   
print(circle.cal_area(r=2)) 
print(sqr.area())   
print(sqr.cal_area(s=4))  

#5. Hybrid Inheritance:
"""
Hybrid inheritance is a combination of different types of inheritance."""
class A:
    def method_A(self):
        return "method_A"

class B(A):
    def method_B(self):
        return "method_B"

class C(A):
    def method_C(self):
        return "method_C"

class D(B, C):
    def method_D(self):
        return "method_D"

obj_d = D()
print(obj_d.method_A())
print(obj_d.method_B())
print(obj_d.method_C())
print(obj_d.method_D())




    