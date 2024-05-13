# import numpy as np
# array_size=10
# random_array=np.random.randint(0,100,array_size)
# print(random_array)


s="hello"
result=map(lambda x:x.upper(),s)
print(list(result))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result=map(lambda x,y : x+y,numbers1,numbers2)
print(list(result))

def square(x):
    return x**2
number=[1,5,8,9]

squred=map(square, number)
print(list(squred))


number_1=[1,5,8,9,12,44,56,89]
sqrt=list(map(lambda x:x**2 ,number_1))
print(sqrt)

string=["hello","world","python"]
upper_string=list(map(str.upper,string))
print(list(upper_string))

numbers = [1, 2, 3, 4, 5]
sqrt=list(map(lambda x:x**2, number))
print(numbers)

# Add corresponding elements from two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list=list(map(lambda x,y:x+y,list1,list2))
print(list)

list_number = [1, 2, 3]
result=map(lambda x:x**2, list_number)
for num in result:
    print(num)

# from functools import partial
# numbers = [1, 2, 3, 4, 5]
# mul_by_2=partial(lambda x,y:x*y ,3)
# result2 = list(map(mul_by_2, numbers))
# print(result2)
    
# # Compute the lengths of strings in a list
# strings = ["apple", "banana", "cherry"]
# lengths = list(map(len, strings))
# print(lengths)
# # Output: [5, 6, 6]
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

people = [Person("Alice"), Person("Bob"), Person("Charlie")]
greetings = map(Person.greet, people)
print(greetings)
# Output: ['Hello, Alice!', 'Hello, Bob!', 'Hello, Charlie!']

my_list = ["1", "7", "8", "6"]
result = map(int, my_list)
print(list(result))
