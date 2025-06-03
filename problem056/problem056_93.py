n, m = map(int, input().split())
A = [[int(e) for e in input().split()] for i in range(n)]
b = []
for i in range(m):
    e = int(input())
    b.append(e)
for i in range(n):
    p = 0
    for j in range(m):
        p += A[i][j] * b[j]
    print(p)