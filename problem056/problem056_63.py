Ia = input().split()
n = int(Ia[0])
m = int(Ia[1])

a = [[0 for midx in range(m)] for nidx in range(n)]
for nidx in range(n):
    A = input().split()
    for midx in range(m):
        a[nidx][midx] = int(A[midx])

b = m * [0]
for bidx in range(m):
    b[bidx] = int(input())

c = n * [0]
for i in range(n):
    for j in range(m):
        c[i] += a[i][j] * b[j]

for i in range(n):
    print(c[i])