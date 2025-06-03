from math import floor

A, B, N = map(int, input().split())
i = min(B - 1, N)
f_i = floor(A * i / B) - A * floor(i / B)

print(f_i)