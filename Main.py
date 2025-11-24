from FileRead import FileRead

from Matrix import matrix
from Container import Ship
from Operation import right, left, up, down

filename = "smallshiptest.txt"
listContainers = FileRead(filename)
ship = Ship(listContainers, False)
m = matrix(ship.listContainers)

for i in range(1, -1, -1):
    for j in range(4):
        if (i == 0 and j == 0):
            print("/n")
        print(m[i][j].location.x, m[i][j].location.y, end = " ")

container = m[0][0]
print(container.location.x)
print(container.location.y)
m = right(m, container.location.x - 1, container.location.y - 1)

print("/n")
print("/n")
for i in range(1, -1, -1):
    for j in range(4):
        if (i == 0 and j == 0):
            print("/n")
        print(m[i][j].description, end = " ")


container = m[0][1]
m = left(m, container.location.x - 1, container.location.y - 1)

print("/n")
print("/n")
for i in range(1, -1, -1):
    for j in range(4):
        if (i == 0 and j == 0):
            print("/n")
        print(m[i][j].description, end = " ")

filename = "smallshiptest2.txt"
listContainers = FileRead(filename)
ship = Ship(listContainers, False)
m2 = matrix(ship.listContainers)

container = m2[0][0]
m2 = up(m2, container.location.x - 1, container.location.y - 1)

print("/n")
print("/n")
for i in range(1, -1, -1):
    for j in range(4):
        if (i == 0 and j == 0):
            print("/n")
        print(m2[i][j].description, end = " ")

container = m2[1][0]
m2 = down(m2, container.location.x - 1, container.location.y - 1)


print("/n")
print("/n")
for i in range(1, -1, -1):
    for j in range(4):
        if (i == 0 and j == 0):
            print("/n")
        print(m2[i][j].description, end = " ")






