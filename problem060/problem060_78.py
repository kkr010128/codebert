n, m, l = [int(s) for s in input().split()]
A = []
B = []
C = [[0 for i in range(l)] for i in range(n)]

for i in range(n):
    A.append([int(s) for s in input().split()])
for i in range(m):
    B.append([int(s) for s in input().split()])

for i,row in enumerate(C):
    for j in range(len(row)):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]


for row in C:
    print(' '.join([str(i) for i in row]))