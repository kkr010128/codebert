n,m = map(int, input().split())
a = [[] for x in range(0, n)]
b = [0 for x in range(0, m)]
for x in range(0, n):
    a[x] = list(map(int, input().split()))
for x in range(0, m):
    b[x] = int(input())
for i in range(0, n):
    c = 0
    for j in range(0, m):
        c += a[i][j] * b[j]
    print(c)