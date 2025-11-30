import heapq

def inSet(matrix, open_set):
    while(len(open_set) != 0):
        _, _, curr_matrix = heapq.heappop(open_set) #returns and removes state
        if(matrix == curr_matrix):
            return True
    return False