n,m,l = map(int, input().split())
A = [[0 for c in range(m)]for r in range(n)]
B = [[0 for c in range(l)]for r in range(m)]
C = [[0 for c in range(l)]for r in range(n)]

for r in range(n):
    A[r][:] = list(map(int, input().split()))
for r in range(m):
    B[r][:] = list(map(int, input().split()))
for row in range(n):
    for col in range(l):
        for i in range(m):
            C[row][col] += A[row][i]*B[i][col]
    print(*C[row][:])
