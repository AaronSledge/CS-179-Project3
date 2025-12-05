import heapq
from State import left_weight
from State import right_weight
from State import balance_calc
from State import con2_balance_check
from State import State
from itertools import count
def inSet(matrix, open_set):
    while(len(open_set) != 0):
        _, _, _, curr_matrix, _ = heapq.heappop(open_set)
        if(curr_matrix == matrix):
            return True
    return False


def getCost(matrix, open_set):
    while(len(open_set) != 0):
        _, gn, _, curr_matrix, _ = heapq.heappop(open_set)
        if(curr_matrix == matrix):
            return gn
    return 0

def addToSetAstar(curr_matrix, new_matrix, container, new_container, cost, actionList, open_set, child, row, col, og_lw, og_rw, tieBreak, maxActions):
    gn = cost + len(actionList)
    lw = left_weight(new_matrix, row, col)
    rw = right_weight(new_matrix, row, col)
    dif_lr = balance_calc(lw, rw)
    curr_state = State(dif_lr, lw, rw, False)

    if(gn > maxActions):
        return gn
    

    if(dif_lr < maxActions or container.location.x == 1):
        hn = dif_lr
    else:
        if(gn <= maxActions):
            hn = maxActions

    if(con2_balance_check(curr_state, og_lw, og_rw)):
        hn = 0
    
    fn = hn + gn
    #print(curr_matrix[i][j].location.x, curr_matrix[i][j].location.y, empty_space.location.x, empty_space.location.y)
    heapq.heappush(open_set, (fn, hn, gn, next(tieBreak), new_matrix, container))
    child.append((curr_matrix, new_matrix, actionList, container, new_container))
    return gn

def addToSetUni(curr_matrix, new_matrix, cost, actionList, open_set, child, row, col, tieBreak):
    gn = cost + len(actionList) #since each cell is 1 min we just add the cost of all actions to get to new position
    #print(curr_matrix[i][j].location.x, curr_matrix[i][j].location.y, empty_space.location.x, empty_space.location.y)
    lw = left_weight(new_matrix, row, col)
    rw = right_weight(new_matrix, row, col)
    #dif_lr = balance_calc(lw, rw)
    fn = gn
    heapq.heappush(open_set, (fn, gn, next(tieBreak), new_matrix, curr_matrix[0][0]))
    child.append((curr_matrix, new_matrix, actionList))
    return gn
