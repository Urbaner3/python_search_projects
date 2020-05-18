
def heuristic(matrix, size, operation, subtrahend):
  score = 0.5
  for i in range(size):
    print(' '.join(str(element) for element in matrix[i]))
  return score
  
