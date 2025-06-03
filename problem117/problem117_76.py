import itertools
import bisect
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_acc = [0] + list(itertools.accumulate(a))
b_acc = [0] + list(itertools.accumulate(b))
ans = 0

for i in range(n+1):
    if k - a_acc[i] >= 0:
        ans = max(ans, i + bisect.bisect(b_acc, k - a_acc[i])-1)
print(ans)
