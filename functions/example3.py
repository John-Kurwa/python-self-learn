# Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.
# Positional arguments must be in the correct order:
def displayInfo(name, age):
    return f"Name: {name}, Age: {age}"
info = displayInfo("Charlie", 30)
print(info)

# Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Pote", age = 5)

# Returning Different Data Types
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments.
# To specify positional-only arguments, add , / after the arguments:
def my_function(a, b, /, c, d):
  print(a, b, c, d)

my_function(1, 2, c=3, d=4)

# Keyword-Only Arguments
# You can specify that a function can have ONLY keyword arguments, adding *, before the keyword arguments:
def my_function(*, b):
  print("Answer:", b)

my_function(b=42)

# Combining Positional-Only and Keyword-Only
# You can combine both argument types in the same function.
# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, c, *, d):
  return a + b + c + d

result = my_function(1, 2, 3, d=4)
print(result)