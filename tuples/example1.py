# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1]

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry", "papaya", "watermelon", "orange", "Pineapple"))  # note the double round-brackets
print(type(thistuple))
print(thistuple)

# Access Tuple Items
print(thistuple[1])
# Tuple Indexing
print(thistuple[2:5])

# Change Tuple Values
changedval = list(thistuple)
changedval[1] = "kiwi"
x = tuple(changedval)

print(x)

# Add Items
fruits = ("apple", "banana", "cherry", "papaya", "watermelon", "orange", "Pineapple")
changedval = list(fruits)
changedval.append("mango")
fruits = tuple(changedval)

print(fruits)
# or
# changedval = ("grapes",)
# fruits += changedval

# print(fruits)

# Remove Items
changedval = list(fruits)
changedval.remove("banana")
fruits = tuple(changedval)

print(fruits)