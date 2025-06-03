import math

A, B, N = list(map(int,input().split()))

def f(x):
    return math.floor(A * x / B) - A * math.floor(x / B)

if B - 1 <= N:
    ans = f(B - 1)
else:
    ans = f(N)
print(ans)