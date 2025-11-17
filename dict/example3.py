# Nested Dictionaries

car1 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car2 = {
"brand": "BMW",
"model": "X3",
"year": 2020
}
car3 = {
"brand": "Fiat",
"model": "500",
"year": 2016
},
mycars = {
"car1": car1,
"car2": car2, 
"car3": car3
}
    
# print(mycars)

# Access Items in Nested Dictionaries
print(mycars["car2"]["model"])