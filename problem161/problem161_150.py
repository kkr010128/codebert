import math

a, b, n = map(int, input().split())
x = b - 1
if x > n:
    x = n
ans = math.floor(a * x / b) - a * math.floor(x / b)
print(ans)
