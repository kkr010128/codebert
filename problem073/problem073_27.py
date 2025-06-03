import math

N = int(input())

s = 0

for a in range(1, N+1):
    s += (N-1)//a

print(s)

