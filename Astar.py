# start from the heaviest side
from State import State
from State import left_weight
from State import right_weight
from State import balance_calc
from State import con1_balance_check
from State import con2_balance_check
from boundCheck import find_nearest_empty_space_left,  find_nearest_empty_space_right, pathToNewContainer, pathFromParkTocontainer, isEmpty, finalContainerToParked, craneMovements
from SetInclusion import  addToSetAstar
from edgeCases import checkOneOnEachSide
from totalContainer import findTotalContainers
import copy
import heapq
from itertools import count
import Container


def Astar(matrix, row, col, maxActions):
    og_lw = left_weight(matrix, row, col)
    og_rw = right_weight(matrix, row, col)
    dif_lr = balance_calc(og_lw, og_rw)
    start_state = State(dif_lr, og_lw, og_rw, False)

    if(dif_lr == 0 or con2_balance_check(start_state, og_lw, og_rw)): #if already balanced we can stop
        start_state.balanced == True
        return [], matrix, [], 0, 0, 0
    

    open_set = []
    closed_set = set()

    tieBreak = count()
    start_matrix = copy.deepcopy(matrix)
    open_set.append((dif_lr, 0, 0, next(tieBreak), start_matrix, start_matrix[0][0]))
    heapq.heapify(open_set)
    matrixSet = set()
    gnTable = {}
    child = []
    moveList = []
    stateList = []
    iteration = 0
    key = tuple(tuple(row) for row in start_matrix)
    gnTable[key] = 0
    matrixSet.add(key)
    while(len(open_set) != 0): 
        fn, hn, cost, _, curr_matrix, parent_container = heapq.heappop(open_set)
        lw = left_weight(curr_matrix, row, col)
        rw = right_weight(curr_matrix, row, col)
        dif_lr = balance_calc(lw, rw)
        curr_state = State(dif_lr, lw, rw, False)
        stateList.append(curr_state) 
        iteration += 1
        if(len(stateList) <= 1): #if only 1 state in list just check if difference is 0 because we have not moved yet
            if(stateList[-1].dif_lr == 0):
                stateList[-1].balanced == True
        else:
            curr_state.balanced = con2_balance_check(curr_state, og_lw, og_rw)
            #if(curr_state.balanced == False):
                #curr_state.balanced = con1_balance_check(curr_state, og_lw, og_rw)
        

        if(checkOneOnEachSide(curr_matrix, row, col) == True): #shipcase 3 edge case, 
            curr_state.balanced = True

        
        if(curr_state.balanced == True):
            finished_matrix = copy.deepcopy(curr_matrix)
            path = []
            totalTime = 0
            totalMoves = 0
            parent = 0
            craneLogic = False
            while(curr_matrix != start_matrix):
                for i in range(len(child)):
                    if (child[i][1] == curr_matrix):
                        if(craneLogic == True):
                            actionList = craneMovements(curr_matrix, child[i][4], parent, row)
                            #path.append((child[i][4], parent, actionList))
                            #moveList.append(actionList)
                            totalTime += len(actionList)
                            totalMoves += 1
                            
                        path.append((child[i][3], child[i][4], child[i][2]))
                        totalTime += len(child[i][2])
                        totalMoves += 1
                        moveList.append(child[i][2]) #add to set of actions for each move
                        curr_matrix = child[i][0] #this gets parent matrix or matrix before move
                        parent = child[i][3]
                        craneLogic = True
            moveList.reverse() #Since we are going from child to parent we need to reverse it to go from start to goal matrix
            path.reverse()
            first_container = path[0][0]
            actionList = pathFromParkTocontainer(first_container, row)
            totalTime += len(actionList)
            totalMoves += 1
            moveList.insert(0, actionList)

            # add initial action info to path
            # # first item needs to be the container that is being moved, and the 2nd item must be the location it is going to
            # right_count = 0
            # down_count = 0
            # for i in range(len(actionList)):
            #     if (actionList[i] == "RIGHT"):
            #         right_count += 1
            #     elif(actionList[i] == "DOWN"):
            #         down_count += 1
            new_loc = path[0][0]
            initial_tuple = (first_container, new_loc, actionList)
            path.insert(0, initial_tuple)

            last_container = path[-1][1]
            actionList = finalContainerToParked(last_container, row)
            moveList.append(actionList)
            totalNumContainers = findTotalContainers(finished_matrix, row, col)
            totalTime += len(actionList)
            totalMoves += 1

            # add last action info to path
            # park location is a container object representing the park position for the crane
            park_loc = Container.Container(Container.Location(8, 1), "0000", "Crane")
            last_tuple = (last_container, park_loc, actionList)
            path.append(last_tuple)
            return moveList, finished_matrix, path, totalTime, totalMoves, totalNumContainers
    
        closed_key = tuple(tuple(row) for row in start_matrix)
        closed_set.add(closed_key)
        #made open_set copies because inSet removes elements in order to check if matrix is in the set
        if (lw > rw): #check left side
            for i in range(row - 1, -1, -1):
                for j in range(int(col / 2)): #covers all cells in lefthand of matrix
                    if(curr_matrix[i][j].description != "UNUSED" and curr_matrix[i][j].description != "NAN"): #check if container is valid to move
                        for k in range(row - 1, -1, -1):
                            for p in range(int(col)):
                                if(curr_matrix[i][j].location.x == 1 and curr_matrix[i + 1][j].description == "UNUSED"):
                                    empty_space = find_nearest_empty_space_right(curr_matrix, row, col, curr_matrix[i][j])
                                    new_matrix = copy.deepcopy(curr_matrix) #make a copy because to path to new container function changes the matrix when we call an operation. Want curr_matrix intact so we can find parent
                                    actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space, row)
                                    key = tuple(tuple(row) for row in new_matrix)
                                    if(key not in matrixSet and key not in closed_set):
                                        gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                        if(gn <= maxActions):
                                            matrixSet.add(key)
                                            gnTable[key] = cost + len(actionList)
                                    elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                        gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                        if(gn <= maxActions):
                                            matrixSet.add(key)
                                            gnTable[key] = cost + len(actionList)
                                
                                elif(curr_matrix[i][j].location.x == row): #if we are at top and we are allowed to move right
                                    if(isEmpty(curr_matrix, curr_matrix[i][j], curr_matrix[k][p]) == True):
                                        empty_space = curr_matrix[k][p]
                                        new_matrix = copy.deepcopy(curr_matrix) #make a copy because to path to new container function changes the matrix when we call an operation. Want curr_matrix intact so we can find parent
                                        actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space, row)
                                        key = tuple(tuple(row) for row in new_matrix)
                                        if(key not in matrixSet and key not in closed_set):
                                            gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                            if(gn <= maxActions):
                                                matrixSet.add(key)
                                                gnTable[key] = cost + len(actionList)
                                        elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                            gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                            if(gn <= maxActions):
                                                matrixSet.add(key)
                                                gnTable[key] = cost + len(actionList)
                                elif(curr_matrix[i + 1][j].description == "UNUSED"):
                                    if(isEmpty(curr_matrix, curr_matrix[i][j], curr_matrix[k][p]) == True):
                                        empty_space = curr_matrix[k][p]
                                        new_matrix = copy.deepcopy(curr_matrix) #make a copy because to path to new container function changes the matrix when we call an operation. Want curr_matrix intact so we can find parent
                                        actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space, row)
                                        key = tuple(tuple(row) for row in new_matrix)
                                        if(key not in matrixSet and key not in closed_set):
                                            gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                            if(gn <= maxActions):
                                                matrixSet.add(key)
                                                gnTable[key] = cost + len(actionList)
                                        elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                            gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                            if(gn <= maxActions):
                                                matrixSet.add(key)
                                                gnTable[key] = cost + len(actionList)
                                else:
                                 continue
                
        else:
            for i in range(row - 1, -1, -1):
                for j in range(int(col / 2), col):
                    if(curr_matrix[i][j].description != "UNUSED" and curr_matrix[i][j].description != "NAN"):
                        for k in range(row - 1, -1, -1):
                            for p in range(int(col)):
                                if(curr_matrix[i][j].location.x == 1 and curr_matrix[i + 1][j].description == "UNUSED"):
                                    empty_space = find_nearest_empty_space_left(curr_matrix, row, col, curr_matrix[i][j])
                                    new_matrix = copy.deepcopy(curr_matrix) #make a copy because to path to new container function changes the matrix when we call an operation. Want curr_matrix intact so we can find parent
                                    actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space, row)
                                    key = tuple(tuple(row) for row in new_matrix)
                                    if(key not in matrixSet and key not in closed_set):
                                        gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                        if(gn <= maxActions):
                                            matrixSet.add(key)
                                            gnTable[key] = cost + len(actionList)
                                    elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                        gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                        if(gn <= maxActions):
                                            matrixSet.add(key)
                                            gnTable[key] = cost + len(actionList)
                                    
                                elif(curr_matrix[i][j].location.x == row): #if we are at top and we are allowed to move left
                                    if(isEmpty(curr_matrix, curr_matrix[i][j], curr_matrix[k][p]) == True):
                                        empty_space = curr_matrix[k][p]
    
                                        new_matrix = copy.deepcopy(curr_matrix) #make a copy because to path to new container function changes the matrix when we call an operation. Want curr_matrix intact so we can find parent
                                        actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space, row)  
                                        key = tuple(tuple(row) for row in new_matrix)
                                        if(key not in matrixSet and key not in closed_set):
                                            gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                            if(gn <= maxActions):
                                                matrixSet.add(key)
                                                gnTable[key] = cost + len(actionList)
                                        elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                            gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                            if(gn <= maxActions):
                                                matrixSet.add(key)
                                                gnTable[key] = cost + len(actionList)
                                elif(curr_matrix[i + 1][j].description == "UNUSED"):
                                    if(isEmpty(curr_matrix, curr_matrix[i][j], curr_matrix[k][p]) == True):
                                        empty_space = curr_matrix[k][p]
                                        new_matrix = copy.deepcopy(curr_matrix) #make a copy because to path to new container function changes the matrix when we call an operation. Want curr_matrix intact so we can find parent
                                        actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space, row)  
                                        key = tuple(tuple(row) for row in new_matrix)
                                        if(key not in matrixSet and key not in closed_set):
                                            gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                            if(gn <= maxActions):
                                                matrixSet.add(key)
                                                gnTable[key] = cost + len(actionList)
                                        elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                            gn = addToSetAstar(curr_matrix, new_matrix, curr_matrix[i][j], empty_space, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions)
                                            if(gn <= maxActions):
                                                matrixSet.add(key)
                                                gnTable[key] = cost + len(actionList)
                                else:
                                 continue
                            

            
            