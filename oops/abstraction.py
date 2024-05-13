
"""Data abstraction is a concept in object-oriented programming that involves hiding 
the complex implementation details of an object and
 exposing only the essential features to the outside world. 
It allows programmers to focus on what an object does rather than how it achieves its functionality. 
Abstraction is achieved through abstract classes and interfaces."""
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def area(self):
        return "cal area of circle"
circle=circle()
print(circle.area()) 



#---------------
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Starting the car engine"

    def stop(self):
        return "Stopping the car engine"

car = Car()
print(car.start())
print(car.stop())


#---------------

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def sleep(self):
        return "Zzzz"

class Dog(Animal):
    def speak(self):
        return "Woof"

dog = Dog()
print(dog.speak())
print(dog.sleep())


#---------------
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"
    #------------------

    from abc import ABC,abstractmethod
class shape(ABC):

  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

class circle(shape): 
  def area(self,r):
      return 3.14*r*r 
  def perimeter(self,r):
      return 2*3.14*r  
circle = circle()
print(circle.area(r=5))
print(circle.perimeter(r=7))

