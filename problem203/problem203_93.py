a, b = map(int, input().split())

import math
aS = math.ceil(a / 0.08)
al = math.floor((a + 1) / 0.08)
bs = math.ceil(b / 0.10)
bl = math.floor((b + 1) / 0.10)

flag = True
for i in range(10000):
    if aS <= i < al and bs <= i < bl:
        print(i)
        flag = False
        break
if flag:
    print(-1)
