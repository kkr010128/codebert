n, m, l = map(int, input().split())
A, B = [], []
C = [[0 for _ in range(l)] for _ in range(n)]
for _ in range(n):
    A.append([int(x) for x in input().split()])
for _ in range(m):
    B.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(l):
        C[i][j] = 0
        for x in range(m):
            C[i][j] += A[i][x] * B[x][j]
for i in C:
    print(*i)