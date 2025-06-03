import math
n =int(input())
x = [int (x) for x in input().split()]
y = [int (y) for y in input().split()]

for p in range(1,4):
    s =sum([abs(x[i]-y[i])**p for i in range(n)])
    s = s**(1/p)
    print("%.6f" % s)

s = max([abs(x[i]-y[i]) for i in range(n)])
print("%.6f" % s)