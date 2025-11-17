# Set items are unordered, unchangeable, and do not allow duplicate values.
# True and 1 is considered the same value:
# False and 0 is considered the same value:
mycars = {"Ford", "BMW", "Volvo", True, 1, False, 0}
print(mycars)

# Get the Length of a Set
print(len(mycars))

# type()
print(type(mycars))

# The set() Constructor
favcars = set(("Audi", "BMW", "Volvo"))
print(favcars)

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

for x in favcars:
    print(x)

# Add Items add()
favcars.add("GTR")
print(favcars)

# Add Multiple Items update()
luxuryCars = {"Range Rover", "Bentley", "Rolls Royce"}
favcars.update(luxuryCars)
print(favcars)

# Add Any Iterable
moreCars = ["Lamborghini", "Ferrari"]
favcars.update(moreCars)
print(favcars)

# Remove Items remove(), discard()
# remove() - If the item to remove does not exist, remove() will raise an error.
# discarrd() - If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
x = favcars.pop()
print(x) # removed item
print(favcars) # set after removal

# clear() - empties the set
# del() - deletes the set completely




