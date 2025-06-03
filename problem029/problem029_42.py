import math

x1, y1, x2, y2 = list(map(float, input().split()))
x = x2 - x1
y = y2 - y1
ans = math.sqrt(pow(x, 2) + pow(y, 2))

print(ans)

