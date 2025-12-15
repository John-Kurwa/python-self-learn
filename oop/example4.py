# Abstraction
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")
    
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
    
animal = Dog("Winter", "German Shepherd")
print(f"{animal.name} the {animal.species} says {animal.sound()}")