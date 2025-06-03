from heapq import heapify, heappop
from collections import deque

x, y, a, b, c = list(map(int, input().split(' ')))
p = list(map(int, input().split(' ')))
q = list(map(int, input().split(' ')))
r = list(map(lambda x: -1 * int(x), input().split(' ')))

p = sorted(p, reverse=True)
q = sorted(q, reverse=True)

s = p[:x] + q[:y]
s.sort()

heapify(r)

for i, _s in enumerate(s):
    if len(r) == 0:
        break

    n = -1 * heappop(r)
    if n > _s:
        s[i] = n

print(sum(s))
