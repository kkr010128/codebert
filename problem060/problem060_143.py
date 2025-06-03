n, m, l = map(int, input().split())
A, B = [], []
C = [[0 for i in range(l)] for j in range(n)]

for i in range(n):
    A.append([int(i) for i in input().split()])

for i in range(m):
    B.append([int(i) for i in input().split()])

B = list(zip(*B))

for i, line_A in enumerate(A):
    for j, line_B in enumerate(B):
        for x, y in zip(line_A, line_B):
            C[i][j] += x * y

for line in C:
    for i, x in enumerate(line):
        if i == l - 1:
            print(x)
        else:
            print(x, end=" ")

