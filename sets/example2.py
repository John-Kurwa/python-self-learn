# union() 
luxury_cars = {"Mercedes", "BMW", "Audi"}
sports_cars = {"Ferrari", "Lamborghini", "BMW"}

combo_cars = luxury_cars | sports_cars
print(combo_cars)

combo_cars = luxury_cars.union(sports_cars)
print(combo_cars)

# Join Multiple Sets
more_cars = {"Porsche", "Maserati"}
all_cars = luxury_cars.union(sports_cars, more_cars)
print(all_cars)

# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.


# update()
more_cars.update(luxury_cars)
print(more_cars)

# Intersection - return a new set, that only contains the items that are present in both sets.
# intersection_update() - will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

# The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
