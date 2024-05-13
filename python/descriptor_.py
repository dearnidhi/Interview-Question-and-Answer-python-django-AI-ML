"""Python descriptors or, more generally, descriptors provide you a powerful technique
 to write reusable code that can be shared between classes. 
They might seem similar to the concept of inheritance, but technically they are not.
 They are a general-purpose way of intercepting attribute access."""
# Example 1: Using a simple descriptor

class DescriptorExample:
    def __get__(self, instance, owner):
        print(f"Getting the value: {instance._value}")
        return instance._value

    def __set__(self, instance, value):
        print(f"Setting the value: {value}")
        instance._value = value

class MyClass:
    def __init__(self, value):
        self._value = value
        self.descriptor = DescriptorExample()

# Create an instance of the class
obj = MyClass(42)

# Access the attribute using the descriptor
obj.descriptor  # Output: Getting the value: 42

# Set the attribute using the descriptor
obj.descriptor = 100  # Output: Setting the value: 100

# Access the attribute directly
print(obj._value)  # Output: 100


# Example 2: Using a property with a descriptor

class DescriptorWithProperty:
    def __init__(self):
        self._value = 0

    def __get__(self, instance, owner):
        print("Getting the value")
        return self._value

    def __set__(self, instance, value):
        print("Setting the value")
        if value < 0:
            raise ValueError("Value must be non-negative")
        self._value = value

    def __delete__(self, instance):
        print("Deleting the value")
        del self._value

class MyClassWithProperty:
    def __init__(self):
        self._descriptor = DescriptorWithProperty()

    @property
    def descriptor(self):
        return self._descriptor

    @descriptor.setter
    def descriptor(self, value):
        self._descriptor.__set__(self, value)

    @descriptor.deleter
    def descriptor(self):
        self._descriptor.__delete__(self)

obj_with_property = MyClassWithProperty()

# Access the attribute using the descriptor
print(obj_with_property.descriptor)  # Output: Getting the value

# Set the attribute using the descriptor
obj_with_property.descriptor = 50  # Output: Setting the value

# Access the attribute using the descriptor after setting
print(obj_with_property.descriptor)  # Output: Getting the value

# Delete the attribute using the descriptor
del obj_with_property.descriptor  # Output: Deleting the value


# Example 3: Read-Only Descriptor

class ReadOnlyDescriptor:
    def __init__(self, value):
        self._value = value

    def __get__(self, instance, owner):
        print("Getting the value")
        return self._value

    def __set__(self, instance, value):
        raise AttributeError("Cannot modify a read-only attribute")

class MyClassReadOnly:
    def __init__(self, value):
        self._readonly = ReadOnlyDescriptor(value)

obj_readonly = MyClassReadOnly(10)
print(obj_readonly._readonly._value)  # Output: Getting the value

try:
    obj_readonly._readonly._value = 20  # Raises AttributeError
    print(obj_readonly._readonly._value)
except AttributeError as e:
    print(e)



# Example 4: Log Access Descriptor

class LogAccessDescriptor:
    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

    def __get__(self, instance, owner):
        print(f"Accessing {self.attribute_name}")
        return instance.__dict__[self.attribute_name]

    def __set__(self, instance, value):
        print(f"Setting {self.attribute_name} to {value}")
        instance.__dict__[self.attribute_name] = value

class MyClassWithDescriptor:
    def __init__(self, value):
        self._value = value
        self.descriptor = LogAccessDescriptor('_value')

# Create an instance of the class
obj = MyClassWithDescriptor(42)

# Access the attribute using the descriptor
obj.descriptor  # Output: Accessing _value

# Set the attribute using the descriptor
obj.descriptor = 100  # Output: Setting _value to 100

# Access the attribute directly
print(obj._value)  # Output: 100
