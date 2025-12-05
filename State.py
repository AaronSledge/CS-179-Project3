# Object called state to store the state of ship and weight.
class State:
    def __init__(self, dif_lr, weight_left, weight_right, balanced):
        self.dif_lr = dif_lr
        self.weight_left = weight_left
        self.weight_right = weight_right
        self.balanced = balanced

def left_weight(matrix, row, col):
    sum = 0
    for i in range(row - 1, -1, -1):
        for j in range(int(col / 2)):
           weight = matrix[i][j].weight[1:6]  
           sum += int(weight)
    return sum

def right_weight(matrix, row, col):
    sum = 0
    for i in range(row - 1, -1, -1):
        for j in range(int(col / 2), col):
           weight = matrix[i][j].weight[1:6]
           sum += int(weight)
    return sum
    
def is_empty(matrix, i, j):
    if (matrix[i][j].description == "UNUSED"):
        return True
    else:
        return False


# takes in the matrices left weight and right weight to create a state object of the ship and return it 
def balance_calc(left_weight, right_weight):
    dif_lr = abs(left_weight - right_weight)
    return dif_lr

# We should check this after each iteration step by step to see if we met the goal state
# this condition will be run multiple times until we can't decrease the weight anymore
# this occurs when the function returns false (which is the goal state)
def con1_balance_check(curr_state, prev_state):
    if(curr_state.dif_lr == 0):
        return True
    
    elif(curr_state.dif_lr == prev_state.dif_lr): #need to check this. May cause problems
        return True
    return False

# Check overall condition at each iteration to see if we potentially meet the goal state faster than con 1
# if the first condition doesn't work, then try this. in theory, this condition should be easier to satisfy than
# the above one
def con2_balance_check(curr_state, og_lw, og_rw):
   if(curr_state.dif_lr <= ((og_lw + og_rw) * 0.10)):
       return True
   return False


