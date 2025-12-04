from FileRead import FileRead

from Matrix import matrix
from Container import Ship
from Operation import right, left, up, down
from Astar import Astar
from UniformCost import Uniform_cost
from edgeCases import checkOneOnEachSide, checkIfNearlyEmpty, checkAllZeroes
import heapq

# smallshiptest.txt stuff
print("--Working with smallshiptest.txt file--")
print()
filename = "smallshiptest.txt"
listContainers = FileRead(filename)
ship = Ship(listContainers, False)
row = 2
col = 2
m = matrix(ship.listContainers, row, col)

for i in range(1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(2):
        # if (i == 0 and j == 0):
        #     print("\n")
        print(f"{m[i][j].description}[{str(m[i][j].location.x).zfill(2)}, {str(m[i][j].location.y).zfill(2)}]", end = " ")
        if(j == 3):
            print()

print()
print(f"--1st Container's Info--")
container = m[0][0]
print(f"{container.description}[{str(container.location.x).zfill(2)}, {str(container.location.x).zfill(2)}]")
m = right(m, container.location.x - 1, container.location.y - 1)

print()
print()
for i in range(1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(2):
        # if (i == 0 and j == 0):
        #     print("\n")
        print(f"{m[i][j].description}[{str(m[i][j].location.x).zfill(2)}, {str(m[i][j].location.y).zfill(2)}]", end = " ")
        if(j == 3):
            print()


container = m[0][1]
m = left(m, container.location.x - 1, container.location.y - 1)

print()
print()
for i in range(1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(2):
        # if (i == 0 and j == 0):
        #     print("\n")
        print(f"{m[i][j].description}[{str(m[i][j].location.x).zfill(2)}, {str(m[i][j].location.y).zfill(2)}]", end = " ")
        if (j == 3):
            print()

# smallshiptest2.txt stuff
print()
print()
print()
print()
print("--Working with smallshiptest2.txt file--")
filename = "smallshiptest2.txt"
listContainers = FileRead(filename)
ship = Ship(listContainers, False)
m2 = matrix(ship.listContainers, row, col)

container = m2[0][0]
m2 = up(m2, container.location.x - 1, container.location.y - 1)

print()
for i in range(1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(2):
        print(f"{m2[i][j].description}[{str(m2[i][j].location.x).zfill(2)}, {str(m2[i][j].location.y).zfill(2)}]", end = " ")
        if (j == 3):
            print()

container = m2[1][0]
m2 = down(m2, container.location.x - 1, container.location.y - 1)


print()
print()
for i in range(1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(2):
        print(f"{m2[i][j].description}[{str(m2[i][j].location.x).zfill(2)}, {str(m2[i][j].location.y).zfill(2)}]", end = " ")
        if (j == 3):
            print()

print()
print()
print()
print()
print("--Working with Astartest1.txt file--")

row = 8
col = 12
filename = "ShipCase4.txt"
listContainers = FileRead(filename)
ship = Ship(listContainers, False)
m3 = matrix(ship.listContainers, row, col)

for i in range(row - 1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(col):
        print(f"{m3[i][j].description}[{str(m3[i][j].location.x).zfill(2)}, {str(m3[i][j].location.y).zfill(2)}]", end = " ")

print()
print()
print()

moveList = []

if(checkAllZeroes(m3, row, col) == False): #check if weights are all zeros. Don't matter how many if that is the case
    if(checkIfNearlyEmpty(m3, row, col) == False): #check if there are only 0 or 1 container
        if(checkOneOnEachSide(m3, row, col) == False): #if they are more than 1, are there 2 with 1 on each side
          #moveList, _ = Uniform_cost(m3, row, col)
          #if(len(moveList) != 0):
            #parked = moveList.pop(-1)
        
          #maxActions = sum(len(i) for i in moveList)
          #print(maxActions)
          moveList, m3, path, totalTime, totalMoves, totalContainers = Astar(m3, row, col, 2)  #if all 3 conditions fail must use A star
          if(len(moveList) != 0):
            moves_without_crane = totalMoves - 2
            time_without_crane = totalTime - len(moveList[0]) - len(moveList[-1])
          #path goes is an array of tuples. It goes [(parent_container, child_container, actions taken to get from parent to child)]

for i in range(row - 1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(col):
        print(f"{m3[i][j].description}[{str(m3[i][j].location.x).zfill(2)}, {str(m3[i][j].location.y).zfill(2)}]", end = " ")

print(moveList)

#closed_set might not work as intended. Maybe make moveList a tuple that contains matrix as well






