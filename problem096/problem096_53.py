import math

n, d = map(int, input().split(" "))

ans = 0
for i in range(n):
    x, y = map(int, input().split(" "))
    double = x ** 2 + y ** 2
    root = math.sqrt(double)
    if root <= d:
        ans += 1

print(ans)
