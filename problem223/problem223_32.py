import sys
from itertools import accumulate

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
a = [(i+1)/2 for i in rl()]
a = [0] + list(accumulate(a))
ans = 0
for i in range(n-k+1):
    ans = max(ans, a[i+k] - a[i])
print(ans)