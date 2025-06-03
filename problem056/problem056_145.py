n, m = list(map(int,input().split()))
array = [list(map(int,input().split())) for i in range(n)]
b = [int(input()) for i in range(m)]
array_2 = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    d = 0
    for j in range(m):
        c = array[i][j]*b[j]
        d += c
    print(d)