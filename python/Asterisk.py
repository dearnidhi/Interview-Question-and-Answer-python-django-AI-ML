#The Asterisk (*) in Python and its use cases
"""
The asterisk sign (*) can be used for different cases in Python:

Multiplication and power operations
Creation of list, tuple, or string with repeated elements
*args , **kwargs , and keyword-only parameters
Unpacking lists/tuples/dictionaries for function arguments
Unpacking containers
Merging containers into list / Merge dictionaries"""

#Multiplication and power operations

# multiplication
result = 7 * 5
print(result)

# power operation
result = 2 ** 4
print(result)

#Creation of list, tuple, or string with repeated elements
zeros=[0]*10
onetwos=[1,5]*3
print(zeros,onetwos)

# tuple
zeros = (0,) * 10
onetwos = (1, 2) * 5
print(zeros)
print(onetwos)

# string
A_string = "A" * 10
AB_string = "AB" * 5
print(A_string)
print(AB_string)

#*args , **kwargs , and keyword-only arguments
""""Use *args for variable-length arguments
Use **kwargs for variable-length keyword arguments
Use *, followed by more function parameters to enforce keyword-only arguments"""

def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
my_function("Hey", 3, [0, 1, 2], name="Alex", age=8)

# Parameters after '*' or '*identifier' are keyword-only parameters and may only be passed using keyword arguments.
def my_function2(name, *, age):
    print(name)
    print(age)

# my_function2("Michael", 5) --> this would raise a TypeError
my_function2("Michael", age=5)

#Unpacking for function arguments
"""Lists/tuples/sets/strings can be unpacked into function arguments with one * if the length matches the parameters.
Dictionaries can be unpacked with two ** if the length and the keys match the parameters."""
def foo(a, b, c):
    print(a, b, c)

# length must match
my_list = [1, 2, 3]
foo(*my_list)

my_string = "ABC"
foo(*my_string)

# length and keys must match
my_dict = {'a': 4, 'b': 5, 'c': 6}
foo(**my_dict)

#Unpacking containers
"""" Unpacking containers
Unpack the elements of a list, tuple, or set into single and multiple remaining elements.
Note that multiple elements are combined in a list,
 even if the unpacked container is a tuple or a set"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

*beginning, last = numbers
print(beginning)
print(last)

print()

first, *end = numbers
print(first)
print(end)

print()
first, *middle, last = numbers
print(first)
print(middle)
print(last)


#Merge iterables into a list / Merge dictionaries
# dump iterables into a list and merge them
my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
my_list = [*my_tuple, *my_set]
print(my_list)

# merge two dictionaries with dict unpacking
dict_a = {'one': 1, 'two': 2}
dict_b = {'three': 3, 'four': 4}
dict_c = {**dict_a, **dict_b}
print(dict_c)