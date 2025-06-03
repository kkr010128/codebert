n, m = list(map(int, input().split()))
A = []
V = []
B = []
for i in range(n):
    A.append(list(map(int, input().split())))
for j in range(m):
    V.append([int(input())])
for i in range(n):
    B.append([0])
    for j in range(m):
            B[i][0] += A[i][j] * V[j][0]
for i in range(n):
    print(B[i][0])