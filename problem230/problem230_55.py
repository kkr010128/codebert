import sys
import bisect
from math import ceil
from itertools import accumulate
n, d, a = [int(i) for i in sys.stdin.readline().split()]
monsters = []
max_x = 0
for i in range(n):
    x, h = [int(i) for i in sys.stdin.readline().split()]
    max_x = max(x, max_x)
    monsters.append([x, h])
monsters.sort(key=lambda x:x[0])
x, h = zip(*monsters)
x_ls = []
for i, (_x, _h) in enumerate(zip(x, h)):
    ind = bisect.bisect_right(x, _x + 2 * d)
    x_ls.append([i, ind, _h])

h = list(h) + [0]
ls = [0 for i in range(n+1)]
cur = 0
res = 0
for i, ind, _h in x_ls:
    if h[i] > 0:
        cur -= ls[i]
    h[i] -= cur
    if h[i] > 0:
        hoge = ceil(h[i] / a)
        res += hoge
        cur += hoge * a
        ls[ind] += hoge * a
print(res)
