my_dict = {"name":"Max", "age":28, "city":"New York"}
#print(my_dict)

# or use the dict constructor, note: no quotes necessary for keys
my_dict2=dict(name="nidi", age=56, address="noida")
#print(my_dict2)


# _my_dict2=my_dict2["name"]
# print(_my_dict2)

# my_dict2["email"]="Nidhi@gmail.com"
# print(my_dict2)

# del my_dict2["name"]
# print(my_dict2)
# print("popped value:", my_dict.pop("age"))
# print(my_dict)
# print("popped item:", my_dict.popitem())
# print(my_dict)

# my_dict.clear()
for key in my_dict2:
    print(key, my_dict2[key])

for key in my_dict.keys():
    print(key)   

for value in my_dict.values():
    print(value) 

for key,value in my_dict.items():
    print(key, value)


dict_org = {"name":"Max", "age":28, "city":"New York"}
dict_copy = dict_org
dict_copy["name"]="nidhi"
print(dict_copy)
print(dict_org)


dict_org = {"name":"Max", "age":28, "city":"New York"}

dict_copy=dict_copy.copy()
dict_copy["age"]=12.7

print(dict_copy)
print(dict_org)


my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Lisa", age=27, city="Boston")
my_dict.update(my_dict_2)
print(my_dict)

c={**my_dict,**my_dict_2}
print(c)

# Python 3.9 or later
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = dict1 | dict2
print(merged_dict)

my_dict = {3: 9, 6: 36, 9:81}
print(my_dict[3], my_dict[6], my_dict[9])

my_tuple = (8, 7)
my_d={my_tuple:78}
print(my_d)

print(my_d[my_tuple])


my_dict_1 = {"name": "Max", "age": 28}
my_dict_2 = {"name": "Alex", "age": 25}
my_dict_1 = {"name": "Max", "age": 28}
nested={"my_dict_A":my_dict_1,
        "my_dict_B":my_dict_2
        }
print(nested)


