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
        if (count == 1):
            filename = CreateLogFile()
        count += 1
        listContainers = FileRead(manifestname)
        ship = Ship(listContainers, False)
        row = 8
        col = 12
        m = matrix(ship.listContainers, row, col)
        totalcontainers = findTotalContainers(m, row, col)
        print(f"{manifestname[0:len(manifestname)-4]} has {totalcontainers} containers\n")
        WriteManifestNameToFile(filename, manifestname, totalcontainers)
        print("Computing a solution... \n")
        totalmoves = 0
        totaltime = 0
        path = []
        new_matrix = []
        if(checkAllZeroes(m, row, col) == False): #check if weights are all zeros. Don't matter how many if that is the case
            if(checkIfNearlyEmpty(m, row, col) == False): #check if there are only 0 or 1 container
                if(checkOneOnEachSide(m, row, col) == False): #if they are more than 1, are there 2 with 1 on each side
                    maxActions = Uniform_cost(m, row, col)
                    moveList, new_matrix, path, totaltime, totalmoves, totalContainers = Astar(m, row, col, maxActions)  #if all 3 conditions fail must use A star
                    #moves_without_crane = totalMoves - 2
                    #time_without_crane = totalTime - len(moveList[0]) - len(moveList[-1])
          #path goes is an array of tuples. It goes [(parent_container, child_container, actions taken to get from parent to child)]
        # runs Astar to find a solution

        if (totalmoves > 1):
            print(f"Solution has been found, it will take \n {totalmoves} moves \n {totaltime} minutes \n")
        else:
            print(f"Solution has been found, it will take \n {totalmoves} move \n {totaltime} minutes \n")
        #moveswithoutcrane = totalmoves - 2
        #timewithoutcrane = totaltime - len(movelist[0]) - len(movelist[-1])
        #WriteTotalMoveTimeToFile(filename, moveswithoutcrane, timewithoutcrane)
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

RunProgram()



