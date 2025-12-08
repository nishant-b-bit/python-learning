class Animal:
    def __init__(self, name):
        self.name = name  # this stores name in the object

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # call Animal.__init__ for this Dog object
        self.breed = breed

dog1 = Dog("Buddy", "Labrador")
print(dog1.name)

