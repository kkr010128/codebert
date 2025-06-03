import math

a, b, n = map(int, input().split())

if n < b:
    print(math.floor(a * n / b) - 5 * math.floor(n / b))
else:
    print(math.floor(a * (b - 1) / b) - 5 * math.floor((b - 1) / b))