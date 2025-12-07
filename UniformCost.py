from State import State
from State import left_weight
from State import right_weight
from State import balance_calc
from State import con1_balance_check
from State import con2_balance_check
from totalContainer import findTotalContainers
from boundCheck import find_nearest_empty_space_left, find_nearest_empty_space_right, pathToNewContainer, pathFromParkTocontainer, isEmpty
from SetInclusion import addToSetUni
from edgeCases import checkOneOnEachSide
import time
import copy #https://www.geeksforgeeks.org/python/copy-python-deep-copy-shallow-copy/
import heapq #https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/
from itertools import count #https://www.geeksforgeeks.org/python/python-itertools-count/#

def Uniform_cost(matrix, row, col):
    og_lw = left_weight(matrix, row, col)
    og_rw = right_weight(matrix, row, col)
    dif_lr = balance_calc(og_lw, og_rw)
    start_state = State(dif_lr, og_lw, og_rw, False)
    start_time = time.time()

    if(dif_lr == 0 or con2_balance_check(start_state, og_lw, og_rw)): #if already balanced we can stop
        start_state.balanced == True
        return [], matrix, [], 0, 0, 0
    

    open_set = []
    closed_set = set()

    tieBreak = count()
    start_matrix = copy.deepcopy(matrix)
    open_set.append((dif_lr, 0, next(tieBreak), start_matrix, start_matrix[0][0]))
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
    numContainers = findTotalContainers(start_matrix, row, col)
    while(len(open_set) != 0): 
        fn, cost, _, curr_matrix, parent_container = heapq.heappop(open_set)
        lw = left_weight(curr_matrix, row, col)
        rw = right_weight(curr_matrix, row, col)
        dif_lr = balance_calc(lw, rw)
        curr_state = State(dif_lr, lw, rw, False)
        stateList.append(curr_state) 
        iteration += 1
        End_time = time.time() - start_time

        if(End_time >= 20):
            return cost * numContainers

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
            while(curr_matrix != start_matrix):
                for i in range(len(child)):
                    if (child[i][1] == curr_matrix):
                        moveList.append(child[i][2]) #add to set of actions for each move
                        curr_matrix = child[i][0] #this gets parent matrix or matrix before move
            moveList.reverse() #Since we are going from child to parent we need to reverse it to go from start to goal matrix
            maxActions = sum(len(i) for i in moveList)
            return maxActions
    
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
                                        gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
                                        matrixSet.add(key)
                                        gnTable[key] = gn
                                    elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                        gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
                                        matrixSet.add(key)
                                        gnTable[key] = cost + len(actionList)
                                
                                elif(curr_matrix[i][j].location.x == row): #if we are at top and we are allowed to move right
                                    if(isEmpty(curr_matrix, curr_matrix[i][j], curr_matrix[k][p]) == True):
                                        empty_space = curr_matrix[k][p]
                                        new_matrix = copy.deepcopy(curr_matrix) #make a copy because to path to new container function changes the matrix when we call an operation. Want curr_matrix intact so we can find parent
                                        actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space, row)
                                        key = tuple(tuple(row) for row in new_matrix)
                                        if(key not in matrixSet and key not in closed_set):
                                            gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
                                            matrixSet.add(key)
                                            gnTable[key] = cost + len(actionList)
                                        elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                            gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
                                            matrixSet.add(key)
                                            gnTable[key] = cost + len(actionList)
                                elif(curr_matrix[i + 1][j].description == "UNUSED"):
                                    if(isEmpty(curr_matrix, curr_matrix[i][j], curr_matrix[k][p]) == True):
                                        empty_space = curr_matrix[k][p]
                                        new_matrix = copy.deepcopy(curr_matrix) #make a copy because to path to new container function changes the matrix when we call an operation. Want curr_matrix intact so we can find parent
                                        actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space, row)
                                        key = tuple(tuple(row) for row in new_matrix)
                                        if(key not in matrixSet and key not in closed_set):
                                            gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
                                            matrixSet.add(key)
                                            gnTable[key] = cost + len(actionList)
                                        elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                            gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
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
                                        gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
                                        matrixSet.add(key)
                                        gnTable[key] = cost + len(actionList)
                                    elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                        gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
                                        matrixSet.add(key)
                                        gnTable[key] = cost + len(actionList)
                                    
                                elif(curr_matrix[i][j].location.x == row): #if we are at top and we are allowed to move left
                                    if(isEmpty(curr_matrix, curr_matrix[i][j], curr_matrix[k][p]) == True):
                                        empty_space = curr_matrix[k][p]
    
                                        new_matrix = copy.deepcopy(curr_matrix) #make a copy because to path to new container function changes the matrix when we call an operation. Want curr_matrix intact so we can find parent
                                        actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space, row)  
                                        key = tuple(tuple(row) for row in new_matrix)
                                        if(key not in matrixSet and key not in closed_set):
                                            gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
                                            matrixSet.add(key)
                                            gnTable[key] = cost + len(actionList)
                                        elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                            gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
                                            matrixSet.add(key)
                                            gnTable[key] = cost + len(actionList)
                                elif(curr_matrix[i + 1][j].description == "UNUSED"):
                                    if(isEmpty(curr_matrix, curr_matrix[i][j], curr_matrix[k][p]) == True):
                                        empty_space = curr_matrix[k][p]
                                        new_matrix = copy.deepcopy(curr_matrix) #make a copy because to path to new container function changes the matrix when we call an operation. Want curr_matrix intact so we can find parent
                                        actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space, row)  
                                        key = tuple(tuple(row) for row in new_matrix)
                                        if(key not in matrixSet and key not in closed_set):
                                            gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
                                            matrixSet.add(key)
                                            gnTable[key] = cost + len(actionList)
                                        elif(key in matrixSet and ((cost + len(actionList)) < gnTable[key])):
                                            gn = addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak)
                                            matrixSet.add(key)
                                            gnTable[key] = cost + len(actionList)
                                else:
                                 continue

            
            