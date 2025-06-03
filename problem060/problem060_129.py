#coding:utf-8
def seki(a, b):
    c = []
    gou = 0
    d = []
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                gou += a[i][k] * b[k][j]

            d.append(gou)
            gou = 0

        c.append(d)
        d=[]
    return c

n, m, l = [int(i) for i in input().rstrip().split()]

a = [list(map(int , input().rstrip().split())) for i in range(n)]
b = [list(map(int , input().rstrip().split())) for i in range(m)]

c = seki(a,b)

for i in c:
    print(" ".join(list(map(str,i))))