# Object called location to store the coordinates of a location read in from the file
class Location:
    def __init__(self, x, y):
        self.row = x
        self.col = y

# Object called container to store the location object, weight, and description of a container read in from file 
class Container:
    def __init__(self, location, weight, description):
        self.location = location
        self.weight = weight 
        self.description = description

# Object called ship to store the list of containers and a boolean to know if the ship is balanced or not yet
class Ship:
    def __init__(self, listContainers, isShipBalanced):
        self.listContainers = listContainers
        self.isShipBalanced = isShipBalanced