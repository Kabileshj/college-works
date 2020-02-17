#function to rotate matrix
def rotate_90(array):
    n = len(array[0])
    for i in range(n//2):
        for j in range(i,n-i-1):
            temp = array[i][j]
            array[i][j] = array[n-1-j][i]
            array[n-1-j][i] = array[n-1-i][n-1-j]
            array[n-1-i][n-1-j] = array[j][n-1-i]
            array[j][n-1-i] = temp

#Driver code
row = int(input())
array = [[] for i in range(row)]
for i in range(row):
    array[i] = [int(j) for j in input().split()]
rotate_90(array)
n = len(array[0])
for i in range(n):
    print(*array[i])