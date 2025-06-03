[n, m, l] = [int(x) for x in raw_input().split()]

A = []
B = []
C = []
counter = 0
while counter < n:
    A.append([int(x) for x in raw_input().split()])
    counter += 1

counter = 0
while counter < m:
    B.append([int(x) for x in raw_input().split()])
    counter += 1

counter = 0
while counter < n:
    C.append([0] * l)
    counter += 1

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += (A[i][k] * B[k][j])

for data in C:
    print(' '.join([str(x) for x in data]))