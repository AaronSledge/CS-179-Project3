def findTotalContainers(finished_matrix, row, col):
    total = 0
    for i in range(row - 1, -1, -1):
        for j in range(col):
            if(finished_matrix[i][j].description != "UNUSED" and finished_matrix[i][j].description != "NAN"):
                total += 1
    
    return total