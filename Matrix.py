import math
from Container import Container
from Container import Location
# input into our matrix a list of container objects

def matrix(listContainer):
  row = 2
  column = 4
  used_set = set()
  matrix = [[Container(Location(i + 1, j + 1), 0, "Test") for i in range(column)] for j in range(row)]

  for i in range(row - 1, -1, -1):
     for j in range(column):
        for k in listContainer:
          if k not in used_set:
            if ((k.location.x == i + 1) and k.location.y == j + 1):
              matrix[i][j] = k
              used_set.add(k)
              break    
  return matrix 