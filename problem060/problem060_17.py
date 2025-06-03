# coding:utf-8
n,m,l = map(int, raw_input().split())
a = [[0 for i in range(m)] for j in range(n)]
b = [[0 for i in range(l)] for j in range(m)]
c = [[0 for i in range(l)] for j in range(n)]
for i in range(n):
    a[i] = map(int, raw_input().split())
for i in range(m):
    b[i] = map(int, raw_input().split())
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]
        else:
            print c[i][j],
    else:
        print

