nml = input().split()
n, m, l = map(int, nml)

A = [[int(i) for i in input().split()] for j in range(n)]
B = [[int(i) for i in input().split()] for j in range(m)]

C = [[0 for i in range(l)] for j in range(n)]

for j in range(n):
    for i in range(l):
        s = 0
        for k in range(m):
            s += A[j][k]*B[k][i]
        C[j][i] = s

for i in C:
    print(' '.join(map(str, i)))