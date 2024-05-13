list1=list()
print(list1)

"""A nested list in Python is a list that appears as an element within another list"""
#nested
a = [[1, 2], [3, 4]]
print(a)
print(a[1])

#List comprehension
aa = [1, 2, 3, 4, 5, 6, 7, 8]
bb=[i*i for i in aa ]  
print(bb)

# a[start:stop:step], default step is 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
a[0:3] = [0] # replace sub-parts, you need an iterable here
print(a)
b = a[::2] # start to end with every second item
print(b)
a = a[::-1] # reverse the list with a negative step:
print(a)
b = a[:] # copy a list with slicing
print(b)


list_org = ["banana", "cherry", "apple"]
list_copy=list_org
list_copy.append(True)
print(list_copy)
print(list_org)


list_org = ["banana", "cherry", "apple"]
list_copy=list_org.copy()
list_copy.append(True)
print(list_copy)
print(list_org)


list_1 = ["banana", "cherry", "apple"]
print(list_1)

# Or create an empty list with the list function
list_2 = list()
print(list_2)

# Lists allow different data types
list_3 = [5, True, "apple"]
print(list_3)

# Lists allow duplicates
list_4 = [0, 0, 1, 1]
print(list_4)

item = list_1[0]
print(item)

# You can also use negative indexing, e.g -1 refers to the last item,
# -2 to the second last item, and so on
item = list_1[-1]
print(item)

# Lists can be altered after their creation
list_1[2] = "lemon"
print(list_1)

qq="hello nidhi"
print(list(qq))

# create list with repeated elements
list_with_zeros = [0] * 5
my_list = ["banana", "cherry", "apple"]


# concatenation
list_concat = list_with_zeros + my_list
print(list_concat)

new_list = sorted(my_list)
print(new_list)

print("Length:", len(my_list))
my_list.append("orange")
my_list.insert(2, "nidhi")
print(my_list)

item = my_list.pop()

print("Popped item: ", item)




# # remove() : removes an item from the list
# my_list.remove("cherry") # Value error if not in the list
# print(my_list)
# # clear() : removes all items from the list
# my_list.clear()
# print(my_list)
my_list.reverse()
print(my_list)

# sort() : sort items in ascending order
my_list.sort()
print('Sorted: ', my_list)

# Lists can be altered after their creation
list_1[2] = "lemon"
print(list_1)

numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
