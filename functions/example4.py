# Python *args and **kwargs
# args
def example_function(*args, **kwargs):
    print("Type of args:", type(args))
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

example_function(1, 2, 3, name="Alice", age=30)

# Using *args with Regular Arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

# Practical Example with *args
def sum_all(*numbers):
   total = 0
   for num in numbers:
      total += num
   return total
result = sum_all(1, 2, 3, 4, 5)
print("Sum:", result)

# Finding Maximum with *args
def find_maximum(*numbers):
   if len(numbers) == 0:
      return None
   maxi =numbers[0]
   for num in numbers:
      if num > maxi:
         maxi = num
      return maxi
  
print(find_maximum(100, 34, 67, 89, 23, 150))

# kwargs
# The **kwargs parameter allows a function to accept any number of keyword arguments.
# Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

def example_function_kwargs(**kwargs):
    print("Type of kwargs:", type(kwargs))
    print("Keyword arguments (kwargs):", kwargs)

example_function_kwargs(name="Bob", age=25, city="New York")

# Using **kwargs with Regular Arguments
def my_kwarg(greeting, **person):
  print(greeting, person['name'], "you are", person['age'], "years old.")
  for key, value in person.items():
    print(f"{key}: {value}")

my_kwarg("Hi",name = "JT", age = "20", city="Los Angeles")

# Combining *args and **kwargs
# The order must be:
# 1. Regular parameters
# 2. *args  
# 3. **kwargs
def combined_function(greeting, *args, **kwargs):
    print("Greeting:", greeting)
    print("Postional arguments:", args)
    print("Keyword arguments:", kwargs)

combined_function("Hello", "Alice", "Bob", age=30, city="New York")

# Unpacking Lists with *
def unpack_list(a, b, c): 
   return a + b + c

numbers = [4, 5, 6]
result =unpack_list(*numbers)
print(result)

# Unpacking Dictionaries with **
def unpack_dict(fname, mname, lname):
   print("Full name:" , fname, mname, lname)
   
name_dict = {"fname": "John", "mname": "F.", "lname": "Kennedy"}
unpack_dict(**name_dict)
