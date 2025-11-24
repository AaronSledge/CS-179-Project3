# Object called location to store the coordinates of a location read in from the file
class Location:
    def __init__(self, number, newNumber, x, y):
        self.number = number
        self.newNumber = newNumber
        self.x = x
        self.y = y

# Object called container to store the location object, weight, and description of a container read in from file 
class Container:
    def __init__(self, location, weight, description):
        self.location = location
        self.weight = weight 
        self.description = description