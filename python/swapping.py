# List of strings
string_list_1 = ["Hello", " ", "World", "!"]

# Joining the list elements into a single string
result_string = ''.join(string_list_1)

# Display the result
print(result_string)



from timeit import default_timer as timer
new_string_list = ["Hello", " ", "World", "!"]
start=timer()

# Joining the list elements into a single string
result_string = ''.join(new_string_list)

# Display the result
end=timer()

print(end - start)
print(result_string)



from timeit import default_timer as timer
my_list=["a"]*100000

start=timer()
a=""
for i in my_list:
    a+=i
end=timer()
print(end - start)



# List of strings
string_list = ["Hello", " ", "World", "!"]

# Joining the list elements into a single string
result_string = ''.join(string_list)

# Display the result
print(result_string)


D = ["I", " ",  "am", " ", "awesome"]
c= "" . join(D)
print(c)