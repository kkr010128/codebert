n, d = map(int, input().split())

import math
count = 0
for i in range(n):
    x, y = map(int, input().split())
    distance = math.sqrt(x**2+y**2)
    if distance <= d:
        count += 1

print(count)