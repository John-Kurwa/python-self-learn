# Access Dictionary Items
# Accessing Items
thisdict = {
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964}
x = thisdict["model"]
print(x)

# get()
z = thisdict.get("model")
print(z)

# Get Keys  (keys())
y = thisdict.keys()
print(y)

x = thisdict.values()
print(x)

# Add a new item
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x)