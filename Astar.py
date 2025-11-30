# start from the heaviest side
from State import State
from State import left_weight
from State import right_weight
from State import balance_calc
from State import con1_balance_check
from State import con2_balance_check
from boundCheck import find_nearest_empty_space_left, find_nearest_empty_space_right, pathToNewContainer
from SetInclusion import inSet
import copy
import heapq


def Astar(matrix, row, col):
    og_lw = left_weight(matrix, row, col)
    og_rw = right_weight(matrix, row, col)
    dif_lr = balance_calc(og_lw, og_rw)
    start_state = State(dif_lr, og_lw, og_rw, False)

    if(dif_lr == 0): #if already balanced we can stop
        start_state.balanced == True
        return [], []
    
    open_set = []
    closed_set = []

    start_matrix = copy.deepcopy(matrix)
    open_set.append((start_state.dif_lr, 0, start_matrix))
    heapq.heapify(open_set)
    heapq.heapify(closed_set)
    child = []
    moveList = []
    stateList = []
    while(len(open_set) != 0): 
        fn, cost, curr_matrix = heapq.heappop(open_set)
        lw = left_weight(curr_matrix, row, col)
        rw = right_weight(curr_matrix, row, col)
        dif_lr = balance_calc(lw, rw)
        curr_state = State(dif_lr, lw, rw, False)

        stateList.append(curr_state) 

        if(len(stateList) <= 1): #if only 1 state in list just check if difference is 0 because we have not moved yet
            if(stateList[-1].dif_lr == 0):
                stateList[-1].balanced == True
        else:
            curr_state.balanced = con1_balance_check(curr_state, stateList[-2])
            if(curr_state.balanced == False):
                curr_state.balanced = con2_balance_check(curr_state, og_lw, og_rw)
    

        if(curr_state.balanced == True):
            finished_matrix = copy.deepcopy(curr_matrix)
            while(curr_matrix != start_matrix):
                for i in range(len(child)):
                    if (child[i][1] == curr_matrix):
                        moveList.append(child[i][2]) #add to set of actions for each move
                        curr_matrix = child[i][0] #this gets parent matrix or matrix before move
            moveList.reverse() #Since we are going from child to parent we need to reverse it to go froms start to goal matrix
            return moveList, closed_set, finished_matrix
        
        heapq.heappush(closed_set, (dif_lr, cost, curr_matrix))
        copy_open_set1 = copy.deepcopy(open_set)
        copy_closed_set1 = copy.deepcopy(closed_set)
        copy_open_set2 = copy.deepcopy(closed_set)
        #made open_set copies because inSet removes elements in order to check if matrix is in the set
        if (lw > rw): #check left side
            for i in range(row - 1, -1, -1):
                for j in range(int(col / 2)): #covers all cells in lefthand of matrix
                    if(curr_matrix[i][j].description != "UNUSED" and curr_matrix[i][j].description != "NAN"): #check if container is valid to move
                        if(curr_matrix[i][j].location.x > 1):  #if stacked, find nearest space on left side of matrix. 
                            empty_space = find_nearest_empty_space_left(curr_matrix, row, col, curr_matrix[i][j])
                        elif(curr_matrix[i + 1][j].description == "UNUSED"): #we can't move this container if there something on top of it
                            empty_space = find_nearest_empty_space_right(curr_matrix, row, col, curr_matrix[i][j])
                        else:
                            continue;
                        
                        
                        new_matrix = copy.deepcopy(curr_matrix) #make a copy because to path to new container function changes the matrix when we call an operation. Want curr_matrix intact so we can find parent
                        actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space)
                        if(inSet(new_matrix, copy_open_set1) == False and inSet(new_matrix, copy_closed_set1) == False):
                            gn = cost + len(actionList) #since each cell is 1 min we just add the cost of all actions to get to new position
                            lw = left_weight(new_matrix, row, col)
                            rw = right_weight(new_matrix, row, col)
                            dif_lr = balance_calc(lw, rw)
                            fn = dif_lr + gn #dif_lr is our herustic
                            heapq.heappush(open_set, (fn, gn, new_matrix))
                            child.append((curr_matrix, new_matrix, actionList))
                        elif(inSet(new_matrix, copy_open_set2) == True and ((cost + len(actionList)) < cost)): #in case we found a better path/update parent and child
                            gn = cost + len(actionList)
                            lw = left_weight(new_matrix, row, col)
                            rw = right_weight(new_matrix, row, col)
                            dif_lr = balance_calc(lw, rw)
                            fn = dif_lr + gn
                            heapq.heappush(open_set, (fn, gn, new_matrix))
                            child.append((curr_matrix, new_matrix, actionList))
        else:
            for i in range(row - 1, -1, -1):
                for j in range(int(col / 2), col):
                    if(curr_matrix[i][j].description != "UNUSED" and curr_matrix[i][j].description != "NAN"):
                        if(curr_matrix[i][j].location.x > 1):  #if stacked, find nearest space on left side of matrix. 
                            empty_space = find_nearest_empty_space_right(curr_matrix, row, col, curr_matrix[i][j])
                        elif(curr_matrix[i + 1][j].description == "UNUSED"):
                            empty_space = find_nearest_empty_space_left(curr_matrix, row, col, curr_matrix[i][j])
                        else:
                            continue

                        new_matrix = copy.deepcopy(curr_matrix)
                        actionList, new_matrix = pathToNewContainer(new_matrix, new_matrix[i][j], empty_space)

                        if(inSet(new_matrix, copy_open_set1) == False and inSet(new_matrix, copy_closed_set1) == False):
                            gn = cost + len(actionList)
                            lw = left_weight(new_matrix, row, col)
                            rw = right_weight(new_matrix, row, col)
                            dif_lr = balance_calc(lw, rw)
                            fn = dif_lr + gn
                            heapq.heappush(open_set, (fn, gn, new_matrix))
                            child.append((curr_matrix, new_matrix, actionList))
                        elif(inSet(new_matrix, copy_open_set2) == True and ((cost + len(actionList)) < cost)):
                            gn = cost + len(actionList)
                            lw = left_weight(new_matrix, row, col)
                            rw = right_weight(new_matrix, row, col)
                            dif_lr = balance_calc(lw, rw)
                            fn = dif_lr + gn
                            heapq.heappush(open_set, (fn, gn, new_matrix))
                            child.append((curr_matrix, new_matrix, actionList))
            

            
            
