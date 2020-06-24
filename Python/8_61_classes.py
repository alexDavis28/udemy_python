class Dog(object):

    """docstring for Dog."""
    # Class Object Attribute
    # Same for any instance of the class
    species = "mammal"


    def __init__(self, breed, name, spots):
        # Attributes
        # Passed into the argument, assigned to object attributes
        self.breed = breed
        self.name = name
        self.spots = spots
