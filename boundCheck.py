import math
from Operation import right, left, up, down
def find_nearest_empty_space_left(matrix, row, col, container):
    distance = math.inf
    for i in range(row - 1, -1, -1):
        for j in range(int(col / 2)): #iterate all containers on left side
            if(matrix[i][j].description == "UNUSED"): #check if container is unused
                if(matrix[i][j].location.x == 1 or matrix[i - 1][j].description != "UNUSED"): #check if matrix is on the ground OR there is something below it to stack on
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
                if(matrix[i][j].location.x == 1 or matrix[i - 1][j].description != "UNUSED"): #check if matrix is on the ground OR there is something below it to stack on
                    manhatten = abs(matrix[i][j].location.x - container.location.x) + abs(matrix[i][j].location.y - container.location.y) #based space off of cloest container given these conditions
                    if (manhatten < distance):
                        distance = manhatten
                        closest_container = matrix[i][j]
    
    return closest_container

def pathToNewContainer(matrix, old_container, new_container):
    old_x = old_container.location.x - 1
    old_y = old_container.location.y - 1
    new_x = new_container.location.x - 1
    new_y = new_container.location.y - 1
    actionList = []
    while(old_x != new_x or old_y != new_y): #keep moving till we reach new spot
        
        if(old_y < new_y): #if we need to move to the right
            if(matrix[old_x][old_y + 1].description == "UNUSED"):  #check if right cell is clear
                matrix = right(matrix, old_x, old_y)
                old_y += 1
                actionList.append("RIGHT")
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
            else:
                matrix = up(matrix, old_x, old_y) #if not go above it
                old_x += 1
                actionList.append("UP") 
    
    return actionList, matrix

            
            
            