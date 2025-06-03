n, m = map(int,input().split())
a = [[0]*m for i in range(n)]
b = [0]*m

for i in range(n):
    a[i] = list(map(int,input().split()))
for j in range(m):
    b[j] = int(input())

c = [0]*n
for i in range(n):
    for j in range(m):
        c[i] += a[i][j] * b[j]

for i in c:
    print(i)
