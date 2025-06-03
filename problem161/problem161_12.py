import math

A, B, N = [int(x) for x in input().split()]
count = min(B-1, N)
a = math.floor(float(A*count)/B) - A * math.floor(float(count)/B)
print(a)



