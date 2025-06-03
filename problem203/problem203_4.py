import math

a, b = list(map(int, input().split()))
n = b * 10
flag = False
while n <= 1009:
    if math.floor(n * 0.1) == b and math.floor(n * 0.08) == a:
        flag = True
        break
    n += 1
print(n) if flag is True else print(-1)
