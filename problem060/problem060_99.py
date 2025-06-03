n, m, l = map(int, input().split())
A = []
B = []
for line in range(n):
    A.append(list(map(int, input().split())))
for line in range(m):
    B.append(list(map(int, input().split())))

C = []
for lines in range(n):
    C.append([sum([A[lines][i] * B[i][j] for i in range(m)]) for j in range(l)])
    print(" ".join(map(str, C[lines])))