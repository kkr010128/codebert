import math
n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
p1 = 0
p2 = 0
p3 = 0
pinf = 0
for i in range(n):
    D = abs(x[i] - y[i])
    p1 += D
    p2 += D**2
    p3 += D**3
    if pinf < D:
        pinf = D
p2 = math.sqrt(p2)
p3 = p3**(1/3)
print("{0:.6f}".format(p1))
print("{0:.6f}".format(p2))
print("{0:.6f}".format(p3))
print("{0:.6f}".format(pinf))
