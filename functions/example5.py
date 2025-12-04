# Decorators
# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.
def changecase(func):
    def wrapper():            
        return func().upper()
    return wrapper
@changecase
def greet():
    return "Hello, World!"
print(greet())

# Multiple Decorator Calls
def changecase_lower(func):
    def wrapper():            
        return func().lower()
    return wrapper

@changecase_lower
def excited_greet():
    return "HELLO, WORLD!"

@changecase_lower
def angry_greet():
    return "I am so angry!"

print(excited_greet())
print(angry_greet())

# Arguments in the Decorated Function
def repeat(func):
    def wrapper(x):
        return func(x) + " " + func(x).upper()
    return wrapper

@repeat
def say_name(name):
    return f"My name is {name}."

print(say_name("JK"))

# Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.
def emphasize(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"
    return wrapper

@emphasize
def intro(name):
    return f"Hello, I am {name}"
print(intro("JK"))

# Decorator With Arguments
# Decorators can accept their own arguments by adding another wrapper level.
def changecase_with_arg(case):
    def decorator(func):
        def wrapper():
            if case == 'upper':
                return func().upper()
            elif case == 'lower':
                return func().lower()
            else:
                return func()
        return wrapper
    return decorator

@changecase_with_arg('upper')
def welcome():
    return "Welcome to the Decorators demo."
print(welcome())

# Multiple Decorators
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

# Preserving Function Metadata
def decorator(func):
    def wrapper():
        return func()
    return wrapper

@decorator
def sample_function():
    return "Sample Output"

print(sample_function.__name__) 

# To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.
# functools.wraps
import functools
def decorator(func):
    @functools.wraps(func)
    def wrapper():
        return func()
    return wrapper

@decorator
def sample_function():
    return "Sample Output"

print(sample_function.__name__)
