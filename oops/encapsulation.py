""" The primary goal of encapsulation is to hide the internal details of an object
 and only expose what is necessary for the outside world to interact with the object."""
class Student:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute

    # Getter method for name
    def get_name(self):
        return self._name

    # Setter method for name
    def set_name(self, new_name):
        self._name = new_name

    # Getter method for age
    def get_age(self):
        return self._age

    # Setter method for age
    def set_age(self, new_age):
        if 0 < new_age < 120:  # Validating age
            self._age = new_age
        else:
            print("Invalid age")

# Usage
student = Student(name="Alice", age=20)

# Accessing attributes through getter methods
print(student.get_name())  # Output: Alice
print(student.get_age())   # Output: 20

# Modifying attributes through setter methods
student.set_name("Bob")
student.set_age(25)

print(student.get_name())  # Output: Bob
print(student.get_age())   # Output: 25



#-----------------------
class Employee:
    def __init__(self, name, salary):
        self._name = name    # Protected attribute
        self._salary = salary  # Protected attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:  # Validating salary
            self._salary = new_salary
        else:
            print("Invalid salary")

# Usage
employee = Employee(name="John", salary=50000)

# Accessing attributes through properties
print(employee.name)    # Output: John
print(employee.salary)  # Output: 50000

# Modifying attributes through property setters
employee.name = "Jane"
employee.salary = 55000

print(employee.name)    # Output: Jane
print(employee.salary)  # Output: 55000


class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # Private attribute

    # Public method to get the balance
    def get_balance(self):
        return self._balance

    # Public method to deposit money
    def deposit(self, amount):
        self._balance += amount

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

# Creating an instance of the BankAccount class
account = BankAccount(balance=1000)

# Accessing public methods to interact with the object
print("Initial Balance:", account.get_balance())

# Depositing and withdrawing money
account.deposit(500)
account.withdraw(200)

# Displaying updated balance
print("Updated Balance:", account.get_balance())

