from collections import deque
from bisect import bisect_right

n, d, a = map(int, input().split())
xh = [tuple(map(int, input().split())) for _ in range(n)]
xh.sort()
x, h = zip(*xh)
h = list(map(lambda x: -(-x//a), h))

s = [0] * (n+1)
ans = 0

for i in range(n):
    add = max(0, h[i] - s[i])
    j = bisect_right(x, x[i]+d*2)
    if j < n: s[j] -= add
    s[i] += add
    ans += add
    s[i+1] += s[i]

print(ans)
