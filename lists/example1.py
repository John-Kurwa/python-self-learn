# changeable
# allow duplicates
# can contain different data types

# The list() Constructor
mycars = list(("Ford", "Chevrolet", "BMW"))
print(mycars)  # ['Ford', 'Chevrolet', 'BMW']

# Access Items
print(mycars[1])  # Chevrolet
# negative indexing
print(mycars[-1]) 
print(list(mycars))
print(len(mycars))
print(type(mycars))
# check if item exists
if "BMW" in mycars:
    print("Yes, 'BMW' is in the mycars list")

# Change Item Value
mycars[0] = "Toyota"
print(mycars)
mycars.append("GTR")
print(mycars)
mycars.insert(1, "Audi")
print(mycars)
# extend list
mycarsextended =["Volvo", "SUbaru"]
mycars.extend(mycarsextended)
print(mycars)

# Add any Iterable to a list
thistuple = ("Honda", "Mazda")
mycars.extend(thistuple)
print(mycars)
