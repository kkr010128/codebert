import sys
import bisect
input = sys.stdin.readline
n, d, a = map(int, input().split())
xh = sorted([tuple(map(int, input().split()))for _ in range(n)])
x_list = [x for x, h in xh]

damage = [0]*(n+1)
ans = 0
for i in range(n):
    x, h = xh[i]
    h -= damage[i]
    if h <= 0:
        damage[i+1] += damage[i]
        continue
    cnt = -(-h//a)
    ans += cnt
    damage[i] += cnt*a
    end_idx = bisect.bisect_right(x_list, x+2*d)
    damage[end_idx] -= cnt*a
    damage[i+1] += damage[i]

print(ans)