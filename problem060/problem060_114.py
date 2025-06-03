A = []
B = []
C = []
n, m, l = map(int, input().strip().split())
[A.append(list(map(int, input().strip().split()))) for x in range(n)]
[B.append(list(map(int, input().strip().split()))) for y in range(m)]
[C.append([0 for zz in range(l)]) for z in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k]*B[k][j]
        if j == l - 1:
            print(C[i][j])
        else:
            print(C[i][j],end=' ')