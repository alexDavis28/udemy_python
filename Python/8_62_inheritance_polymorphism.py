# Inheritance uses classes you already have to make more classes

class Animal():
    """docstring for Animal."""

    def __init__(self):
            print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):
    # This is known as a derived class as it takes feature from the parent class
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    # to overwrite a method make a new method with the same name
    def who_am_i(arg):
        print("I am a dog")

myDog = Dog()
myDog.eat()
myDog.who_am_i()

# POLYMORPHISM
# Polymorphism is the way in which different object classes can share the same method name

class Fish():
    """docstring for Fish."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says blub!"


class Cat():
    """docstring for Cat."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow"

niko = Fish("niko")
felix = Cat("felix")
print(niko.speak())
print(felix.speak())
# These have the same name but do different things
# eg:
for pet in [niko, felix]:
    print(pet.speak())
# or
def pet_speak(pet):
    print(pet.speak())

# ABSTRACT classes
# abstract classes are ones that act as base classes and are never initalised
class BaseAnimal():
    """docstring for baseAnimal."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
        # Do this so people have to overwrite this function in a subclass

class Horse(BaseAnimal):
    """docstring for Horse."""

    def speak(self):
        return self.name + " says neigh!"
