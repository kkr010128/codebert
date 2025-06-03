import math

N, X, T = map(int, input().split())

a = math.ceil(N/X)
b = a * T

print(b)
