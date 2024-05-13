#1-----------------
#2------------------
c="uppppssssssss"
d=''.join(reversed(c))
print(d)

#3------------------
e="hi my school is unique"
f=e[::-1]
print(f)  

#4------------------
my_string = "     Hello World "
print(my_string.strip())
print(len(my_string))

# Upper and lower cases
print(my_string.upper())
print(my_string.lower())

# startswith and endswith
print("hello".startswith("he"))
print("hello".endswith("llo"))


message = "Hello World"
new_message = message.replace("World", "Universe")
print(new_message)

my_string = "how are you doing"
aa=my_string.split()
print(aa)

my_string = "one,two,three"
a = my_string.split(",")
print(a)

my_list = ['How', 'are', 'you', 'doing']
ta=''.join(my_list).split()
print(ta)

# concat strings with +
greeting = "Hello"
name = "Tom"
sen= greeting  + ' ' + name
print(sen)


my_string = "Hello World"

# get character by referring to index
b = my_string[0]
print(b)

my_string____ = "Hello World"

# get character by referring to index
b = my_string____[2:3]
print(b)

my_stringr = """Hello 
World"""
print(my_stringr)

# backslash if you want to continue in the next line
my_string = "Hello \
World"
print(my_string)