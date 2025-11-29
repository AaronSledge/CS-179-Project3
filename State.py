# Object called state to store the state of ship and weight.
class State:
    def __init__(self, dif_lr, weight_left, weight_right):
        self.dif_lr = dif_lr
        self.weight_left = weight_left
        self.weight_right = weight_right

# takes in the matrices left weight and right weight to create a state object of the ship and return it 
def balance_calc(left_weight, right_weight):
    dif_lr = abs(left_weight - right_weight)
    ship_status = State(dif_lr, left_weight, right_weight)
    return ship_status

# We should check this after each iteration step by step to see if we met the goal state
# this condition will be run multiple times until we can't decrease the weight anymore
# this occurs when the function returns false (which is the goal state)
def con1_balance_check(curr_state, prev_state):
    if (curr_state.dif_lr < prev_state.dif_lr):
        return True
    return False

# Check overall condition at each iteration to see if we potentially meet the goal state faster than con 1
# if the first condition doesn't work, then try this. in theory, this condition should be easier to satisfy than
# the above one
def con2_balance_check(curr_state):
    con_2 = (curr_state.weight_left + curr_state.weight_right) * 0.10
    if (curr_state.dif_lr <= con_2):
        return True
    return False

