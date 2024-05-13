"""In Python, a decorator is a design pattern that allows you to extend or 
modify the behavior of functions or classes without permanently modifying their code.
 Decorators are implemented using functions or classes that wrap around other functions or 
 classes to add additional functionality."""
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}.")

# Using the class methods
MyClass.static_method()
MyClass.class_method()



from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
# Running the Flask app
if __name__ == '__main__':
    app.run()


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Using the decorated function
say_hello()


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

# Using the decorated function
say_hello()

