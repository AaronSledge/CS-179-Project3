from FileRead import FileRead

from Matrix import matrix
from Container import Ship
from Operation import right, left, up, down
from FinalManifest import CreateFinalManifest
from ScreenToUser import UserInteraction

# smallshiptest.txt stuff
print("--Working with smallshiptest.txt file--")
print()
filename = "smallshiptest.txt"
listContainers = FileRead(filename)
ship = Ship(listContainers, False)
m = matrix(ship.listContainers)
original_matrix = m

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
final_matrix = m

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


actionList = []
action_tuple = [(original_matrix, final_matrix, actionList)]
CreateFinalManifest(filename, action_tuple)

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
original_matrix = m2

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
final_matrix = m2

print()
print()
for i in range(1, -1, -1):
    print(f"Row: {i+1}")
    for j in range(4):
        print(f"{m2[i][j].description}[{str(m2[i][j].location.x).zfill(2)}, {str(m2[i][j].location.y).zfill(2)}]", end = " ")
        if (j == 3):
            print()

actionList = []
action_tuple = [(original_matrix, final_matrix, actionList)]
CreateFinalManifest(filename, action_tuple)



# Test for FinalManifest function
print()
print()
print()
print()
print("--Working with ShipCase3.txt file--")

#filename = "ShipCase3.txt"

filename = input("Enter a Manifest: ")

# need to add all this stuff to the ScreenToUser function to make code cleaner
listContainers = FileRead(filename)
ship = Ship(listContainers, False)
original_matrix = matrix(ship.listContainers)

filename_solution = "ShipCase3_Solution.txt"
listContainers_solution = FileRead(filename_solution)
ship_solution = Ship(listContainers_solution, False)
final_matrix = matrix(ship_solution.listContainers)

actionList = []
sol_time = 26
sol_moves = 3

action_tuples = [(original_matrix, final_matrix, actionList)]

UserInteraction(filename, action_tuples, sol_time, sol_moves)

CreateFinalManifest(filename, action_tuples)





