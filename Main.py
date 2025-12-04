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

def RunProgram():

    count = 1
    while True:
        manifestname = input("Enter a Manifest: ")
        if (count == 1):
            filename = CreateLogFile()
        count += 1
        listContainers = FileRead(manifestname)
        ship = Ship(listContainers, False)
        row = 8
        col = 12
        maxActions = 10
        m = matrix(ship.listContainers, row, col)
        totalcontainers = findTotalContainers(m, row, col)
        print(f"{manifestname[0:len(manifestname)-4]} has {totalcontainers} containers\n")
        WriteManifestNameToFile(filename, manifestname, totalcontainers)
        print("Computing a solution... \n")
        movelist, new_matrix, path, totaltime, totalmoves, totalcontainers = Astar(m, row, col, maxActions)
        if (totalmoves > 1):
            print(f"Solution has been found, it will take \n {totalmoves} moves \n {totaltime} minutes \n")
        else:
            print(f"Solution has been found, it will take \n {totalmoves} move \n {totaltime} minutes \n")
        moveswithoutcrane = totalmoves - 2
        timewithoutcrane = totaltime - len(movelist[0]) - len(movelist[-1])
        WriteTotalMoveTimeToFile(filename, moveswithoutcrane, timewithoutcrane)
        WritePathToFile(filename, path, totalcontainers)
        WriteCycleFinished(filename, manifestname)
        userIn = input("Enter S to stop")
        if (userIn == "S" or userIn == "s"):
            print("End program")
            exit()

RunProgram()



