import math
n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))
for p in [1.0,2.0,3.0]:
    s = 0
    for i in range(n):
        s += abs(x[i]-y[i])**p
    print(pow(s,1.0/p))
print(max([abs(x[i]-y[i]) for i in range(n)]))