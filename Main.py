from FileRead import FileRead

from Matrix import matrix
from Container import Ship
from Operation import right, left, up, down

# smallshiptest.txt stuff
print("--Working with smallshiptest.txt file--")
print()
filename = "smallshiptest.txt"
listContainers = FileRead(filename)
ship = Ship(listContainers, False)
m = matrix(ship.listContainers)

for i in range(1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(4):
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
    for j in range(4):
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
    for j in range(4):
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
m2 = matrix(ship.listContainers)

container = m2[0][0]
m2 = up(m2, container.location.x - 1, container.location.y - 1)

print()
for i in range(1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(4):
        print(f"{m2[i][j].description}[{str(m2[i][j].location.x).zfill(2)}, {str(m2[i][j].location.y).zfill(2)}]", end = " ")
        if (j == 3):
            print()

container = m2[1][0]
m2 = down(m2, container.location.x - 1, container.location.y - 1)


print()
print()
for i in range(1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(4):
        print(f"{m2[i][j].description}[{str(m2[i][j].location.x).zfill(2)}, {str(m2[i][j].location.y).zfill(2)}]", end = " ")
        if (j == 3):
            print()






