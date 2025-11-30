from FileRead import FileRead

from Matrix import matrix
from Container import Ship
from Operation import right, left, up, down
from Astar import Astar
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

row = 2
col = 6
filename = "Astartest1.txt"
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

moveList, closed_set, m3 = Astar(m3, row, col)

for i in range(row - 1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(col):
        print(f"{m3[i][j].description}[{str(m3[i][j].location.x).zfill(2)}, {str(m3[i][j].location.y).zfill(2)}]", end = " ")

print(moveList)
#closed_set might not work as intended. Maybe make moveList a tuple that contains matrix as well






