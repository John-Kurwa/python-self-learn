# Inheritance
class Animal:
    def __init__(self, name, species, ):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat") # Call the parent constructor
        self.color = color

    def meow(self):
        return f"{self.name} says Meow!" # Overriding method
    
class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name, species="Bird")
        self.wing_span = wing_span

    def chirp(self):
        return f"{self.name} says Chirp!"
    
class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name, species="Fish")
        self.water_type = water_type

    def splash(self):
        return f"{self.name} is splashing in the {self.water_type} water!"

# Creating objects of the subclasses    
dog1 = Dog("Glock", "Husky")
cat1 = Cat("Whiskers", "Tabby")
bird1 = Bird("Tweety", "15 cm")
fish1 = Fish("Nemo", "salt")

# Testing the classes and methods
print(dog1.bark())
print(cat1.meow())
print(bird1.chirp())
print(fish1.splash())        