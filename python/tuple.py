"""
A tuple is an immutable ordered collection of elements in Python.
 Immutable means that once a tuple is created, its contents cannot be changed, 
 added, or removed. Tuples are similar to lists,
 but they are enclosed within parentheses () instead of square brackets []"""

# compare the size
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# compare the execution time of a list vs. tuple creation statement
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

a = ((0, 1), ('age', 'height'))
print(a)
print(a[0])


tuple_1 = ("Max", 28, "New York")
name,age,city=tuple_1
print(name)
print(age)
print(city)

my_tuple = (0, 1, 2, 3, 4, 5)
item_first,*items_between,item_last=my_tuple
print(item_first)
print(items_between)
print(item_last)

# a[start:stop:step], default step is 1
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
b = a[::2] # start to end with every second item
print(b)
b = a[::-1] # reverse tuple
print(b)


string="nidhiya"
string_to_tuple=tuple(string)
print(string_to_tuple)

my_list = ['a', 'b', 'c', 'd']
a=tuple(my_list)
print(a)

my_tuple = (1,2,3) + (4,5,6)
print(my_tuple)
my_tuple = ('a','p','p','l','e',)
print(len(my_tuple))
# count(x) : Return the number of items that is equal to x
print(my_tuple.count('p'))

# index(x) : Return index of first item that is equal to x
print(my_tuple.index('l'))

tuple_1 = ("Max", 28, "New York")
tuple_2 = "Linda", 25, "Miami" # Parentheses are optional

if "Miami" in tuple_2:
    print("yes")
else:
    print("no")


item = tuple_1[0]
print(item)
# You can also use negative indexing, e.g -1 refers to the last item,
# -2 to the second last item, and so on
item = tuple_1[-1]
print(item)
tuple_1 = ("Max", 28, "New York")
tuple_2 = "Linda", 25, "Miami" # Parentheses are optional

# Special case: a tuple with only one element needs to have a comma at the end, 
# otherwise it is not recognized as tuple
tuple_3 = (25,)
print(tuple_1)
print(tuple_2)
print(tuple_3)

# Or convert an iterable (list, dict, string) with the built-in tuple function
tuple_4 = tuple([1,2,3])
print(tuple_4)


x, y, z = (1, 2, 3)
print(x, y, z)  # Output: 1 2 3

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_tuple = tuple(my_dict.keys())
value_tuple = tuple(my_dict.values())
print(key_tuple)
print(value_tuple)


