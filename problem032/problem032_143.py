import math
n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
for p in range(1,4):
    s = [math.fabs(x[i]-y[i])**p for i in range(n)]
    z = math.pow(sum(s), 1/p)
    print("{:.6f}".format(z))
t = [math.fabs(x[i]-y[i]) for i in range(n)]
print("{:.6f}".format(max(t)))