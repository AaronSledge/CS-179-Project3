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

    crane_loc_row = 9
    crane_loc_col = 1

    if(dif_lr == 0): #if already balanced we can stop
        start_state.balanced == True
        return [], []
    
    # make a copy of the tontainer matrix
    start_matrix = copy.deepcopy(matrix)

    # what do I need? a priority queue, a list of all the best actions made

    pq = []
    best_actions = []

    # push all possible first actions to the heap queue
    for 