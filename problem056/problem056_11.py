n, m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for y in range(n)]
b = [int(input()) for x in range(m)]
c = [0 for i in range(n)]

for i in range(n):
    c[i] = sum([a[i][x] * b[x] for x in range(m)])

for i in c:
    print(i)