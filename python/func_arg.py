"""In Python, function arguments are the values 
that you pass to a function when you call it. There are
different types of function arguments, including positional 
arguments, keyword arguments, default arguments, and variable-length arguments.
"""


#Positional Arguments:

"""These are the most common type of arguments.
The order in which you pass the values matters.
The function parameters receive values based on their position."""

def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)
print(result)


def mul_number(c,d):
    return c*d
result_2=mul_number(4,8.9)
print(result_2)

#Keyword Arguments:

"""You can explicitly specify which parameter 
receives which value by using the parameter names.
Order doesn't matter in this case."""

def greet(name,greeting):
    return f"{greeting},{name}"
message=greet(name="nidhis" ,greeting="hello")
print(message)


#Default Arguments:

"""You can provide default values for parameters in case the caller doesn't pass a value for that parameter.
Parameters with default values must come after parameters without default values.

"""

def power(base, exponent=2):
    return base **exponent
result_3=power(3)
print(result_3)

#Variable-Length Arguments:

"""Functions can accept a variable number of arguments.
Two types: *args for variable positional arguments and **kwargs for variable keyword arguments."""

def print_args(*args, **kwargs):
        print("Positional arguments:", args)
        print("Keword arguments:", kwargs)
result_4=print_args(1,2,3,5, name="sachin", age=78)
print(result_4)

    



