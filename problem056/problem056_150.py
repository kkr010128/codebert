n,m = map(int,input().split())
matrix = [[0 for i in range(m)] for j in range(n)]
b = [0 for i in range(m)]
c = [0 for i in range(n)]
for i in range(0,n):
    matrix[i] = list(map(int,input().split()))
for i in range(0,m):
    b[i] = int(input())
for i in range(0,n):
    for j in range(0,m):
        c[i] += matrix[i][j]*b[j]
    print(c[i])
    

