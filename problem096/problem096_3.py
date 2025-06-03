#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import math

n, d = map(int, input().split())
cnt = 0
for i in range(n):
    x, y = map(int, input().split())
    dis = math.sqrt(x ** 2 + y ** 2)
    if dis <= d:
        cnt += 1
print(cnt)
