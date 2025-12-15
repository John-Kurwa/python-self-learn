# __init__() Method
# Without the __init__() method, you would need to set properties manually for each object:
class Person:
    def __init__(self):
        pass

class Employee:
    def  __init__(self, name, id):
        self.name = name
        self.id = id
emp1 = Employee("John", 101)
emp2 = Employee("Jane", 102)

print(f"Employee 1: Name = {emp1.name}, ID = {emp1.id}")

class Car:
    def __init__(self, name, model, price, year):
        self.name = name
        self.model = model
        self.price = price
        self.year = year
car1 = Car("Toyota", "Camry", 24000, 2020)
car2 = Car("Honda", "Civic", 22000, 2019)

print(car1.model)

# The __str__() Method 
# The __str__() method is a special method that controls what is returned when the object is printed:
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Book Name: {self.name} by {self.author}"    
        
book1 = Book("1984", "George Orwell")
print(book1)

# Multiple Methods in a Class
class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def start(self):
        return f"{self.name} {self.model} is starting."

    def stop(self):
        return f"{self.name} {self.model} is stopping."
    
car1 = Car("Ford", "Mustang")
print(car1.start())