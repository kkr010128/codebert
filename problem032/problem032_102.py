import math as ma

n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

d = [int(0)]*4 #m,e,p3,t
tmp = int(0)
tmp2 = int(0)
tmp3 = [int(0)]*n

for i in range(n):
    d[0] += abs(x[i]-y[i])
    tmp += (x[i]-y[i])**2
    tmp2 += (abs(x[i]-y[i]))**3
    tmp3[i] = abs(x[i]-y[i])

d[1] = ma.sqrt(tmp)
d[2] = (tmp2)**(1/3)
d[3] = max(tmp3)

for i in range(4):
    print(d[i])

