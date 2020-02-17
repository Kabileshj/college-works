#function for changing rows and columns
def setZeroes(matrix):
    points = [[i,j] for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == 0]
    for i, a in enumerate(points):
        for k in range(len(matrix[0])):
            matrix[a[0]][k] = 0
        for k in range(len(matrix)): 
            matrix[k][a[1]] = 0 

#driver code
row = int(input())
matrix = [[] for i in range(row)]
for i in range(row):
    matrix[i] = [int(j) for j in input().split()]
setZeroes(matrix)
for i in range(row):
    print(*matrix[i])