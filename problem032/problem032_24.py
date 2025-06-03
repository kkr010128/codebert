import math
n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
p1 = p2 = p3 = p = 0
for x,y in zip(x,y):
    d = abs(x-y)
    p1 += d
    p2 += d**2
    p3 += d**3
    if d>p: p = d
print('{0:.5f}\n{1:.5f}\n{2:.5f}\n{3:.5f}'.format(p1,math.sqrt(p2),math.pow(p3,1/3),p))

