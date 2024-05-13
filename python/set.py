
"""Set: A set in Python is mutable, meaning you can
 add or remove elements after the set is created. 
 You can use methods like add() and remove() to modify the set


Frozenset: A frozenset, on the other hand, is immutable.
 Once a frozenset is created, you cannot add or remove elements.
   It remains fixed throughout its lifetime.
# The following is not allowed:
# a.add(5)
# a.remove(1)
# a.discard(1)
# a.clear() ."""

a = frozenset([0, 1, 2, 3, 4])


# Also no update methods are allowed:
# a.update([1,2,3])
# Other set operations work
odds = frozenset({1, 3, 5, 7, 9})
evens = frozenset({0, 2, 4, 6, 8})
print(odds.union(evens))
print(odds.intersection(evens))
print(odds.difference(evens))

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issubset(setB))
print(setB.issubset(setA)) # True


set_org = {1, 2, 3, 4, 5}
# now modifying the copy also affects the original
set_copy=set_org
set_copy.update([6,7,8,9])
print(set_copy)
print(set_org)




# use copy() to actually copy the set
set_org_= {1, 2, 3, 4, 5}
set_copy_=set_org_.copy()
set_copy_.update([9,10,11,12,13])
print(set_copy_)
print(set_org_)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# update() : Update the set by adding elements from another set.
setA.update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# update() : Update the set by adding elements from another set.
setA.update(setB)
print(setA)

# intersection_update() : Update the set by keeping only the elements found in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.intersection_update(setB)
print(setA)

# difference_update() : Update the set by removing elements found in another set.
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.difference_update(setB)
print(setA)

# symmetric_difference_update() : Update the set by only keeping the elements found in either set, but not in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.symmetric_difference_update(setB)
print(setA)

# Note: all update methods also work with other iterables as argument, e.g lists, tuples
# setA.update([1, 2, 3, 4, 5, 6])

my_set = {"apple", "banana", "cherry"}
for i in my_set:
    print(i)

if "apple" in my_set:
    print('yes')    

    
# remove(x): removes x, raises a KeyError if element is not present
my_set = {"apple", "banana", "cherry"}
my_set.remove("apple")
print("new set",my_set)

# KeyError:
# my_set.remove("orange")

# discard(x): removes x, does nothing if element is not present
my_set.discard("cherry")
my_set.discard("blueberry")
print(my_set)

# clear() : remove all elements
my_set.clear()
print(my_set)

# pop() : return and remove a random element
a = {True, 2, False, "hi", "hello"}
print(a.pop())
print(a)


#ADD
my_set_u=set()
my_set_u.add("nidhi")
my_set_u.add(99.9)
my_set_u.add(False)
print(my_set_u)
my_set_u.add(True)
print(my_set_u)

my_set = {"apple", "banana", "cherry"}
print(my_set)

# or use the set function and create from an iterable, e.g. list, tuple, string
my_set_2 = set(["one", "two", "three"])
my_set_2 = set(("one", "two", "three"))
print(my_set_2)

my_set_3 = set("aaabbbcccdddeeeeeffff")
print(my_set_3)

# careful: an empty set cannot be created with {}, as this is interpreted as dict
# use set() instead
a = {}
print(type(a))

a = set()
print(type(a))

# mylist = ['apple', 'banana', 'cherry']
# x = frozenset(mylist)
# x[1] = "strawberry"
# print(mylist)

#Freeze the list, and make it unchangeable:

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)