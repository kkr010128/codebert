import math

n, d = [int(n) for n in input().split(' ')]

cnt = 0
for i in range(n):
    x, y = [int(n) for n in input().split(' ')]
    if math.sqrt(x*x + y*y) <= d:
        cnt += 1
print(cnt)
