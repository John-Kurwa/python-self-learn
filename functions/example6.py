# lambda functions
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
x = lambda m, n: m * n
print(x(5, 8))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def tuesday(n):
    return lambda a: a * n

myweekday = tuesday(3)
days = tuesday(4)

print(myweekday(7))
print(days(7))

# Lambda with Built-in Functions
# map(), filter(), and sorted()
# map() function
slots = [8, 10, 16, 22, 18, 6]
doubled = list(map(lambda x: x * 2, slots))

print(doubled)

# filter() function
salary = [5000, 7000, 3000, 9000, 6000, 4000]
high_salary = list(filter(lambda y: y >= 5000, salary))

print(high_salary)

# sorted() function
votes = [("A2452", 25), ("J4567", 20), ("A3955", 30)]
sorted_votes = sorted(votes, key=lambda vote: vote[1], reverse=True)

print(sorted_votes)

# Sort strings by length:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
sorted_fruits = sorted(fruits, key=lambda fruit: len(fruit), reverse=False)

print(sorted_fruits)