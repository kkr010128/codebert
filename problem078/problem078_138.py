import math

n = int(input())
a = pow(10, n, 10**9+7)
b = pow(9, n, 10**9+7)
c = pow(9, n, 10**9+7)
d = pow(8, n, 10**9+7)
print((a-b-c+d) % (10**9+7))