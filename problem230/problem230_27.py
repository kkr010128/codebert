from math import ceil
from bisect import bisect_right
n, d, a = (int(x) for x in input().split())
xh = []
for _ in range(n):
    x, h = (int(x) for x in input().split())
    xh.append([x, h])
xh = sorted(xh, key=lambda x: x[0])
cnt = 0
dmg = [0] * (n + 1)
for i, (x, h) in enumerate(xh):
    dmg[i] += dmg[i - 1]
    h -= dmg[i]
    if h <= 0:
        continue
    num = ceil(h / a)
    dmg[i] += num * a
    idx = bisect_right(xh, [x + 2 * d, float('inf')])
    dmg[idx] -= num * a
    cnt += num
print(cnt)