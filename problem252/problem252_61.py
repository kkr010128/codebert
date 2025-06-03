n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

import bisect
def is_ok(x):
    cnt = 0
    for i, a in enumerate(A):
        j = bisect.bisect_left(A, x-a)
        cnt += n-j
    if cnt >= m:
        return True
    else:
        return False

l = 0
r = 2*10**5+1
while l+1 < r:
    c = (l+r)//2
    if is_ok(c):
        l = c
    else:
        r = c

from itertools import accumulate
B = [0]+A
B = list(accumulate(B))
ans = 0
cnt = 0
for a in A:
    j = bisect.bisect_left(A, l-a)
    cnt += (n-j)
    ans += B[-1]-B[j]+a*(n-j)
ans -= (cnt-m)*l
print(ans)