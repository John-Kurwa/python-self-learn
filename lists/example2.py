# loop lists
mycars = ["Ford", "Chevrolet", "BMW"]
for car in mycars:
    print(car)

# list comprehension
newcar = []
for car in mycars:
    if 'o' in car:
        newcar.append(car)

print(newcar)

# using list comprehension
newcar = [car for car in mycars if 'o' in car]
print(newcar)

# copy() list method
mycars = ["Ford", "Chevrolet", "BMW"]
favcars = mycars.copy()
print(favcars)

# Make a copy of a list with list()
favcars = list(mycars)
print(favcars)

# Make a copy of a list with slicing (:)
favcars = mycars[:]
print(favcars)

# List concatenation
cars = ["Porsche", "Volvo", "Audi"]
favcars = ["GMC", "BMW", "Chevrolet"]
# allcars = cars + favcars
# print(allcars)

for car in cars:
    cars.append(favcars)
print(favcars)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

list1.extend(list2)
print(list1)

