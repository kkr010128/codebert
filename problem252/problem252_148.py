import bisect
from itertools import accumulate

def func(x):
    cnt = 0
    for i in a:
        index = bisect.bisect_left(a, x - i)
        cnt += N - index
    if cnt >= M:
        return True
    else:
        return False

N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ar = sorted(a, reverse=True)
b = [0] + list(accumulate(ar))

MIN = 0
MAX = 2 * 10 ** 5 + 1
while MAX - MIN > 1:
    MID = (MIN + MAX) // 2
    if func(MID):
        MIN = MID
    else:
        MAX = MID

ans = 0
cnt = 0
for i in ar:
    index = bisect.bisect_left(a, MIN - i)
    ans += i * (N - index) + b[N - index]
    cnt += N - index
print(ans - (cnt - M) * MIN)