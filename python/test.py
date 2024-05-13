def sum_of_num(num):
    return sum(num)
list=[8,9,33,66,90,1000]
result=sum_of_num(list)
print(result)
#-------------------------

def reverse_string(S):
    return S[::-1]
word="hello bharat"
result_1=reverse_string(word)
print(result_1)

#-----------------------

word_2="malyalam bolo yar"
print(word_2[::-1])

#------------------------
def palindrom_num(word_3):
    return word_3 ==word_3[::-1]
words = "Nidhi"
result_2= palindrom_num(words)
print(result_2)
#--------------------------

def remove_duplicate(lst):
    return set(lst)
duplicate_list=[6,7,7,8,9,"nidhi","nidhi",6,5]
dupl_var=remove_duplicate(duplicate_list)
print(dupl_var)



try:
    x=1/0
except ZeroDivisionError:
    print("can not divided")    


#------------------
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12
#-----------------

def factorial_num(n):
  if n==0:
    return 1
  else:
     return n*factorial_num(n-1)
  print(factorial_num(4))

  #-------------------

def decorator_func(func):
     def wrapper():
        print("hey yaar")
        func()
        print("something")
    
     return wrapper
@decorator_func
def say_hello():
    print("NNNidhi")
say_hello()

#-------------------

#-------------------

squar_no=[x**2 for x in range(10)]
print(squar_no)

#---------------------


def function_example(*args, **kwargs):
    for arg in args:
        print(arg)
    for key , value in kwargs.items():
        print(f"{key} in value {value}")
function_example(3,8,9 , p=4 ,q=5)   

#-----------------------
def my_generator():
    yield 1
    yield 2
gen=my_generator()
for i in gen:
    print(i)
#-----------------
    def my_decorator(fun):
        def wrapper():
         print("something happend")
        fun()
        print("some thing happend after creating function")
        return wrapper
    @my_decorator 
    def say_hello():
        print("sayhello")  
    say_hello()
  #----------------------
    def my_generator3(n):
        for i in range(n):
            yield i 
    gen2= my_generator3(5)  
    for number in gen2:
        print(number)
#-------------------------

def my_gen_4():
    yield 1
    yield 2
    yield 3
gen_4=  my_gen_4()
for i in gen_4:
    print(i)  
#----------------------------------     
'''x = [1, 2, 3]

if isinstance(x,(list,tuple)):
    print("x is a list")
else:
    print("x is not a list and tuple")  '''


my_list = [1, 2, 3, 4, 5]

# Iterable: Has __iter__() method
iterable_object = iter(my_list)

# Iterator: Implements __next__() method
print(next(iterable_object))  # Output: 1
print(next(iterable_object))  # Output: 2

    
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)

def myfunc(n):
  return len(n)

xx = map(myfunc, ('apple', 'banana', 'cherry'))
print(xx)



def ne_map(a,b):
   return a+b
# Two tuples
tuple1 = ('apple', 'banana', 'cherry')
tuple2 = ('orange', 'lemon', 'pineapple')

objj=map(ne_map,tuple1,tuple2)
#result=list(objj)
print(objj)
#print(result)


numbers=[1,2,3,4,5,6]
sqr=map(lambda x: x**2,numbers)
#print(list(sqr))



d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3={**d1 , **d2}
print(d3)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"

# Creating an instance of Person
person = Person("Alice", 30)

# Using the print() function will invoke __str__
print(person)  # Output: Person: Alice, Age: 30


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Call the fibonacci function and print the result
result = fibonacci(5)
print(result)

   
                 

            
