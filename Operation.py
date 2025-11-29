from Container import Location
import copy

def right(matrix, x, y):
    if (matrix[x][y + 1].description == "UNUSED"):
        matrix[x][y + 1].description = matrix[x][y].description
        matrix[x][y + 1].weight = matrix[x][y].weight
        matrix[x][y].description = "UNUSED"
        matrix[x][y].weight = "{00000}"
    return matrix

def left(matrix, x, y):
    if (matrix[x][y - 1].description == "UNUSED"):
        matrix[x][y - 1].description = matrix[x][y].description
        matrix[x][y - 1].weight = matrix[x][y].weight
        matrix[x][y].description = "UNUSED"
        matrix[x][y].weight = "{00000}"
    return matrix

def up(matrix, x, y):
    if (matrix[x + 1][y].description == "UNUSED"):
        matrix[x + 1][y].description = matrix[x][y].description
        matrix[x + 1][y].weight = matrix[x][y].weight
        matrix[x][y].description = "UNUSED"
        matrix[x][y].weight = "{00000}"
    return matrix

def down(matrix, x, y):
    if (matrix[x - 1][y].description == "UNUSED"):
        matrix[x - 1][y].description = matrix[x][y].description
        matrix[x - 1][y].weight = matrix[x][y].weight
        matrix[x][y].description = "UNUSED"
        matrix[x][y].weight = "{00000}"
    return matrix


