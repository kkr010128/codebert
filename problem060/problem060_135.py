n, m, l = map(int, input().split(" "))

A = []
for i in range(n):
    A.append(list())
    X = list(map(int, input().split(" ")))
    for j in range(m):
        A[i].append(list())
        A[i][j] = X[j]

B = []
for i in range(m):
    B.append(list())
    X = list(map(int, input().split(" ")))
    for j in range(l):
        B[i].append(list())
        B[i][j] = X[j]

C = []
for i in range(n):
    C.append(list())
    for j in range(l):
        C[i].append(list())
        C[i][j] = 0 
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]
    print(" ".join([str(x) for x in C[i]]))