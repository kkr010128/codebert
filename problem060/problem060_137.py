f = open(0)
N, M, L = map(int, f.readline().split())
A = [list(map(int, f.readline().split())) for i in range(N)]
B = [list(map(int, f.readline().split())) for i in range(M)]
C = [[0]*L for i in range(N)]
for i in range(N):
    for j in range(L):
        C[i][j] = str(sum(A[i][k]*B[k][j] for k in range(M)))
for line in C:
    print(*line)
