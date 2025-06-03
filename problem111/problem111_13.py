import math
N = int(input())
A = sorted(list(map(int, input().split())),reverse=True)
s = A[0]

for i in range(1,N-1):
    s += A[math.ceil(i/2)]

print(s)