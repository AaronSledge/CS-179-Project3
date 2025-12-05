from FileRead import FileRead

from Matrix import matrix
from Container import Ship
from Operation import right, left, up, down
from Astar import Astar
from UniformCost import Uniform_cost
from edgeCases import checkOneOnEachSide, checkIfNearlyEmpty, checkAllZeroes
import heapq
from LogFile import CreateLogFile
from LogFile import WriteManifestNameToFile
from LogFile import WriteTotalMoveTimeToFile
from LogFile import WritePathToFile
from LogFile import WriteCycleFinished
from LogFile import WriteComment
from totalContainer import findTotalContainers
from FinalManifest import CreateFinalManifest
from ScreenToUser import UserInteraction
import os

def RunProgram():

    count = 1
    while True:
        manifestname = input("Enter a Manifest: ")
        if (manifestname == ""):
            print("\nNothing was input as the Manifest name.\n")
        elif (len(manifestname) < 5):
            print("\nManifest name is not long enough.\n")
        elif (manifestname[-4:] != ".txt"):
            print("\nManifest name must end with .txt.\n")
        else:
            if (count == 1):
                filename = CreateLogFile()
            count += 1
            listContainers = FileRead(manifestname)
            if listContainers is not None:
                ship = Ship(listContainers, False)
                row = 8
                col = 12
                m = matrix(ship.listContainers, row, col)
                totalcontainers = findTotalContainers(m, row, col)
                if (totalcontainers < 16):
                    print(f"{manifestname[0:len(manifestname)-4]} has {totalcontainers} containers\n")
                    WriteManifestNameToFile(filename, manifestname, totalcontainers)
                    print("Computing a solution... \n")

                    #maxActions, time_so_far = Uniform_cost(m, row, col)

                    maxActions = 10
                    # runs Astar to find a solution
                    movelist, new_matrix, path, totaltime, totalmoves, totalcontainers = Astar(m, row, col, maxActions)

                    if (totalmoves > 1):
                        print(f"Solution has been found, it will take \n {totalmoves} moves \n {totaltime} minutes \n")
                    else:
                        print(f"Solution has been found, it will take \n {totalmoves} move \n {totaltime} minutes \n")

                    WriteTotalMoveTimeToFile(filename, totalmoves, totaltime)
                    WritePathToFile(filename, path, totalmoves)

                    manifestname = os.path.splitext(os.path.basename(manifestname))[0]
                    manifestname += "OUTBOUND.txt"
                    WriteCycleFinished(filename, manifestname)

                    # creates the final manifest file that will be emailed to the captain
                    CreateFinalManifest(manifestname, new_matrix)

                    userIn = input("Enter S to stop \n")
                    if (userIn == "S" or userIn == "s"):
                        print("End program")
                        exit()
                else:
                    print("\nThe Manifest has more than 16 containers.\n")
                    continue

RunProgram()



