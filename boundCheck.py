import math
from Operation import right, left, up, down


def find_nearest_empty_space_left(matrix, row, col, container):
    distance = math.inf
    for i in range(row - 1, -1, -1):
        for j in range(int(col / 2)): #iterate all containers on left side
            if(matrix[i][j].description == "UNUSED"): #check if container is unused
                if(matrix[i][j].location.x == 1 or matrix[i - 1][j].description != "UNUSED"): #check if container is on the ground OR there is something below it to stack on
                    if(matrix[i - 1][j].description != container.description):
                        manhatten = abs(matrix[i][j].location.x - container.location.x) + abs(matrix[i][j].location.y - container.location.y) #based space off of cloest container given these conditions
                        if (manhatten < distance):
                            distance = manhatten
                            closest_container = matrix[i][j]
    return closest_container

def find_nearest_empty_space_right(matrix, row, col, container):
    distance = math.inf
    for i in range(row - 1, -1, -1):
        for j in range(int(col / 2), col): #iterate all containers on left side
            if(matrix[i][j].description == "UNUSED"): #check if container is unused
                if(matrix[i][j].location.x == 1 or matrix[i - 1][j].description != "UNUSED"): #check if container is on the ground OR there is something below it to stack on
                    if(matrix[i - 1][j].description != container.description):
                        manhatten = abs(matrix[i][j].location.x - container.location.x) + abs(matrix[i][j].location.y - container.location.y) #based space off of cloest container given these conditions
                        if (manhatten < distance):
                            distance = manhatten
                            closest_container = matrix[i][j]
    return closest_container

def isEmpty(matrix, old_container, new_container):
    i = new_container.location.x - 1
    j = new_container.location.y - 1

    
    if(new_container.description == "UNUSED"):
        if(new_container.location.x == 1):
            return True
        elif(matrix[i - 1][j].description != "UNUSED"):
             if(matrix[i - 1][j].description != old_container.description):
                return True
    
    return False


def pathToNewContainer(matrix, old_container, new_container, row):
    old_x = old_container.location.x - 1
    old_y = old_container.location.y - 1
    new_x = new_container.location.x - 1
    new_y = new_container.location.y - 1
    actionList = []

    #print(matrix[old_x][old_y].location.x, matrix[old_x][old_y].location.y, matrix[new_x][new_y].location.x, matrix[new_x][new_y].location.y,)
    while(old_x != new_x or old_y != new_y): #keep moving till we reach new spot
        if(old_y < new_y): #if we need to move to the right
            if(matrix[old_x][old_y + 1].description == "UNUSED"):  #check if right cell is clear
                matrix = right(matrix, old_x, old_y)
                old_y += 1
                actionList.append("RIGHT")
            elif(old_x == row - 1 and matrix[old_x][old_y + 1] != "UNUSED"):
                actionList.append("UP")
                actionList.append("RIGHT")
                actionList.append("RIGHT")
                actionList.append("DOWN")
                matrix[old_x][old_y + 2].description = matrix[old_x][old_y].description
                matrix[old_x][old_y + 2].weight = matrix[old_x][old_y].weight
                matrix[old_x][old_y].description = "UNUSED"
                matrix[old_x][old_y].weight = "{00000}"
                old_y += 2
            else:
                matrix = up(matrix, old_x, old_y) #if not go above it
                old_x += 1
                actionList.append("UP")
        elif(old_y == new_y and old_x != new_x): # we are right position but too high move down
            matrix = down(matrix, old_x, old_y)
            old_x -= 1
            actionList.append("DOWN")
        elif(old_y > new_y): # we need to move left
            if(matrix[old_x][old_y - 1].description == "UNUSED"): #check if left cell is avilaible
                matrix = left(matrix, old_x, old_y)
                old_y -= 1
                actionList.append("LEFT")
            elif(old_x == row - 1 and matrix[old_x][old_y - 1] != "UNUSED"):
                actionList.append("UP")
                actionList.append("LEFT")
                actionList.append("LEFT")
                actionList.append("DOWN")
                matrix[old_x][old_y - 2].description = matrix[old_x][old_y].description
                matrix[old_x][old_y - 2].weight = matrix[old_x][old_y].weight
                matrix[old_x][old_y].description = "UNUSED"
                matrix[old_x][old_y].weight = "{00000}"
                old_y -= 2
            
            else:
                matrix = up(matrix, old_x, old_y) #if not go above it
                old_x += 1
                actionList.append("UP") 
    
    return actionList, matrix
def pathFromParkTocontainer(old_container, row):
    old_x = row
    old_y = 1
    actionList = []
    
    start_x = old_container.location.x
    start_y = old_container.location.y

    while (old_y < start_y):
        old_y += 1
        actionList.append("RIGHT")
    
    while (old_x > start_x):
        old_x -= 1
        actionList.append("DOWN")
    
    return actionList

def finalContainerToParked(last_container, row):
    old_x = last_container.location.x
    old_y = last_container.location.y

    parked_x = row + 1
    parked_y = 1

    actionList = []
    while(old_x < parked_x):
        old_x += 1
        actionList.append("UP")
    
    while(old_y > parked_y):
        old_y -= 1
        actionList.append("LEFT")
    
    return actionList

def craneMovements(matrix, old_container, new_container, row):
    old_x = old_container.location.x - 1
    old_y = old_container.location.y - 1
    new_x = new_container.location.x - 1
    new_y = new_container.location.y - 1
    print(old_x, old_y, new_x, new_y)
    actionList = []
    while(old_x != new_x or old_y != new_y): #keep moving till we reach new spot
        if(old_y < new_y): #if we need to move to the right
            if(matrix[old_x][old_y + 1].description == "UNUSED"):  #check if right cell is clear
                old_y += 1
                actionList.append("RIGHT")
            elif(old_x == row - 1 and matrix[old_x][old_y + 1] != "UNUSED"):
                actionList.append("UP")
                actionList.append("RIGHT")
                actionList.append("RIGHT")
                actionList.append("DOWN")
                old_y += 2
            else:
                old_x += 1
                actionList.append("UP")
        elif(old_y == new_y and old_x != new_x): # we are right position but too high move down
            old_x -= 1
            actionList.append("DOWN")
        elif(old_y > new_y): # we need to move left
            if(matrix[old_x][old_y - 1].description == "UNUSED"): #check if left cell is avilaible
                old_y -= 1
                actionList.append("LEFT")
            elif(old_x == row - 1 and matrix[old_x][old_y - 1] != "UNUSED"):
                actionList.append("UP")
                actionList.append("LEFT")
                actionList.append("LEFT")
                actionList.append("DOWN")
                old_y -= 2
            
            else:
                old_x += 1
                actionList.append("UP") 

    return actionList
    
