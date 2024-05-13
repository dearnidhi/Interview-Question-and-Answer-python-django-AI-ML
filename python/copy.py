
#Assignment operation

""""This will only create a new variable with 
the same reference. Modifying one will affect the other."""
list_a = [1, 2, 3, 4, 5]
list_b=list_a
list_a[0]=-10
print(list_a)
print(list_b)

# #Shallow copy
# import copy
"""", it creates a new object, but does not create 
copies of the objects contained within the original object"""
# # Original list
# list_c = [1, 2, 3, 4, 5]

# # Creating a shallow copy
# list_d = copy.copy(list_c)

# # Modifying an element in the shallow copy
# list_d[1] = -100

# # Displaying both the original and shallow copy
# print("Original List:", list_c)
# print("Shallow Copy:", list_d)
import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.copy(list_a)

# affects the other!
list_a[0][0]= -10
print(list_a)
print(list_b)

#Deep Copy
"""" it creates a new object and recursively copies all
 objects contained within the original object"""

list_e = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_f=copy.deepcopy(list_e)
list_e[0][1]=-2.5
print(list_e)
print(list_f)


