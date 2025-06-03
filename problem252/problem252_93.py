# 上からm番目がx
# x以上のヒトがm人以上、x+1以上のヒトがm-1人以下
# x以上のヒトがm人以上となる最大のx
from bisect import bisect_left
from itertools import accumulate
import sys

input = sys.stdin.buffer.readline


n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ok = 0
ng = 3 * (10 ** 5)

B = [0] + A[::-1]
C = list(accumulate(B))

while ng - ok > 1:
    mid = (ok + ng) // 2
    cnt = 0
    for i in range(n):
        gendo = mid - A[i]
        position = bisect_left(A, gendo)
        if position == n:
            continue
        kosuu = n - position
        cnt += kosuu
    if cnt >= m:
        ok = mid
    else:
        ng = mid
ans = 0
cnt = m
for i in range(n):
    gendo = ok - A[i]
    position = bisect_left(A, gendo)
    if position == n:
        continue
    kosuu = n - position
    ans += C[kosuu] + kosuu * A[i]
    cnt -= kosuu
ans += cnt * ok
print(ans)
