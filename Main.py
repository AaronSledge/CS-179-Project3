from FileRead import FileRead

from Matrix import matrix
from Container import Ship
from Operation import right

filename = "smallshiptest.txt"
listContainers = FileRead(filename)
ship = Ship(listContainers, False)
m = matrix(ship.listContainers)

for i in range(1, -1, -1):
    for j in range(4):
        if (i == 0 and j == 0):
            print("/n")
        print(i, j, end = " ")

container = m[0][0]
print(container.location.x)
print(container.location.y)
m = right(m, container.location.x, container.location.y)

print("/n")
print("/n")
for i in range(1, -1, -1):
    for j in range(4):
        if (i == 0 and j == 0):
            print("/n")
        print(m[i][j].description, end = " ")








