A = []
b = []
row = 0
col = 0
row, col = map(int, raw_input().split())
A = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    r = map(int, raw_input().split())
    for index, j in enumerate(r):
        A[i][index] = j

for i in range(col):
    b.append(int(raw_input()))

for i in A: 
    ret = 0 
    for j,k in zip(i,b):
        ret += j*k
    print ret