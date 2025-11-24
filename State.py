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
def con1_balance_check(curr_state, prev_state):
    if (curr_state.balance_con < prev_state.balance_con):
        return True

# Check overall condition at each iteration to see if we potentially meet the goal state faster than con 1
def con2_balance_check(curr_state):
    con_2 = (curr_state.weight_left + curr_state.weight_right) * 0.10
    if (curr_state.balance_con < con_2):
        return True

