from itertools import accumulate
from bisect import bisect
n, m, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
a = list(accumulate(a))
b = list(accumulate(b))
ans = 0
for i in range(n+1):
    if a[i] > k:
        break
    ans = max(ans, i+bisect(b, k-a[i])-1)
print(ans)