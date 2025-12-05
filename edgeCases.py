def checkIfNearlyEmpty(matrix, row, col):
    count = 0
    for i in range(row - 1, -1, -1):
        for j in range(col):
            if(matrix[i][j].description != "UNUSED" and matrix[i][j].description != "NAN"):
                count += 1
            
            if(count >= 2):
                return False
    return True

def checkOneOnEachSide(matrix, row, col):
    count = 0
    for i in range(row - 1, -1, -1):
        for j in range(int(col / 2)):
            if(matrix[i][j].description != "UNUSED" and matrix[i][j].description != "NAN"):
                count += 1
            
            if(count >= 2):
                return False

    count = 0
    for i in range(row - 1, -1, -1):
        for j in range(int(col / 2), col):
            if(matrix[i][j].description != "UNUSED" and matrix[i][j].description != "NAN"):
                count += 1
            
            if(count >= 2):
                return False
    

    return True


def checkAllZeroes(matrix, row, col):
    for i in range(row - 1, -1, -1):
        for j in range(col):
            weight = matrix[i][j].weight[1:6]
            if(int(weight) != 0):
                return False
    
    return True
    
