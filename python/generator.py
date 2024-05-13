"""In Python, a generator is a special type of iterator that allows you to iterate over a sequence of items,
generating them on-the-fly rather than storing them in memory all at once.
Generators are defined using a function that contains one or more yield statements.
When a generator function is called, it returns an iterator object that can be used to iterate over the values produced by the generator."""


def yours_generator():
    yield 1
    yield 2
    yield 3
gen = yours_generator()
for value in gen:
    print(value)    

def mygen():
    yield 2*3
    yield 7
    yield 6
gen=mygen()  
print(next(gen))  
print(next(gen))
print(next(gen))

"""What is the purpose of the yield statement in Python?

Answer: The yield statement is used in generator functions
 to yield a value to the caller while suspending the function's execution.
   It allows the function to produce a sequence of values one at a time,
     pausing and resuming as needed."""


"""yield:- It takes the place of a function's return in order
 to pause the execution of the function without losing any local variables."""

"""return:-It exits a function and returns a value to its caller."""


def char_generator(s):
    for char in s:
        yield char
# Using the generator
my_string = "hello nidhiya"
gen = char_generator(my_string)  # Creating a generator object
for char in gen:  # Iterating over the generator object
    print(char)

     
