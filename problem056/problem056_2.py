n, m = map(int, raw_input().split())
A = []
b = []
for i in range(n):
    A += [map(int, raw_input().split())]
for i in range(m):
    b += [input()]
for i in range(n):
    C = 0
    for j in range(m):
        C += A[i][j] * b[j]
    print C