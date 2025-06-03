import math
X = int(input())
N = 100
t = 0
while N<X:
    t+=1
    N = N*101//100
print(t)
