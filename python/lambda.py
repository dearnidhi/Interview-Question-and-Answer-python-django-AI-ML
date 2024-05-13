x=lambda x,y :x+y
print(x(2,4))

x=lambda x :x*x
print(x(9))


def myfunc(n):
    return lambda x : x*n
obj1=myfunc(3)
print(obj1(6))

obj2=myfunc(4)
print(obj2(9))



points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
sort=sorted(points2D,key=lambda x : x[1])
print(sort)

mylist = [- 1, -4, -2, -3, 1, 2, 3, 4]
sorted_by_abs=sorted(mylist , key= lambda x : abs(x))
print(sorted_by_abs)


numbers = [1, 2, 3, 4, 5]
squared_numbers=list(map(lambda x : x**2, numbers))
print(squared_numbers)

words = ["apple", "banana", "cherry"]
uppercase_words = list(map(lambda x: x.upper(), words))
print(uppercase_words)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_no=list(filter(lambda x : x % 2 == 0, numbers))
print(even_no)

words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda x : len(x) > 5, words))
print(long_words)


from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)

words = ["Hello", " ", "world", "!"]
concatenated_string = reduce(lambda x, y: x + y, words)
print(concatenated_string)
