#Answer to all your problems
# This code is my own take on this video's interview question
# https://www.youtube.com/watch?v=4tYoVx0QoN0&ab_channel=Cl%C3%A9mentMihailescu
# Big ups to Clément Mihailescu and Ben Awad
import random
def create_matrix():
    row = random.randint(4, 10)
    col = random.randint(4, 10)
    matrix = [[0 for j in range(col)] for x in range(row)]
    for r in matrix:
       for c in range(col):
           r[c] = random.randint(0, 1)
    return matrix
def is_edge(i,j,matrix):
    return i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix[0])-1
def is_in_matrix(i,j,matrix):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])
def get_neighbours(i,j,matrix):
    lst = []
    if is_in_matrix(i-1, j, matrix) and matrix[i-1][j] == 1:
        lst.append((i-1,j))
    if is_in_matrix(i, j-1, matrix) and matrix[i][j-1] == 1:
        lst.append((i,j-1))
    if is_in_matrix(i+1, j, matrix) and matrix[i+1][j] == 1:
        lst.append((i+1,j))
    if is_in_matrix(i, j+1, matrix) and matrix[i][j+1] == 1:
        lst.append((i,j+1))
    return lst

def is_connected_to_edge(i,j,matrix):
    if (matrix[i][j] == 0):
        return False
    if (is_edge(i,j,matrix)):
        return True
    Q = [(i,j)]
    finished = []
    while (True):
        for x,y in get_neighbours(Q[0][0],Q[0][1],matrix):
            if (x,y) not in finished and (x,y) not in Q:
                Q.append((x,y))
        finished.append(Q[0])
        Q.pop(0)
        if len(Q) == 0:
            break
    #print(finished)
    return any([True for x,y in finished if is_edge(x,y,matrix)])
        
matrix = create_matrix()
def print_matrix(matrix):
    for row in matrix:
        print(row)
print_matrix(matrix)
print("")
for i in range(1,len(matrix)-1):
    for j in range(1,len(matrix[0])-1):
        if matrix[i][j] == 1 and not is_connected_to_edge(i, j, matrix):
            matrix[i][j] = 0
print_matrix(matrix)
        
        
