# Polymorphism
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def sound(self):
        return "Woof!"
    
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def sound(self):
        return "Meow!"
    
class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return "Moo!"
    
class Fish:
    def __init__(self, name, water_type):
        self.name = name
        self.water_type = water_type

    def sound(self):
        return "Blub!"
    
animals = [Dog("Beta", "Belian Malinois"),
           Cat("Whiskers", "Siamese"),
              Cow("Bessie", 5), 
                Fish("Nemo", "salt")]
for animal in animals:
    print(f"{animal.name} says {animal.sound()}")

print("------------------------------")

# Inheritance Class Polymorphism
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        return "Some sound"
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def sound(self):
        return "Meow!"
    
class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, species="Cow")
        self.age = age

    def sound(self):
        return "Moo!"
    
class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name, species="Fish")
        self.water_type = water_type

    def sound(self):
        return "Blub!"
    
animals = [Dog("Visa", "Cane Corso"),
           Cat("Mittens", "Persian"),
              Cow("Daisy", 4),
                Fish("Dory", "fresh")]

for animal in animals:
    print(f"{animal.name} the {animal.species} says {animal.sound()}")