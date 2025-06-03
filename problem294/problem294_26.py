import itertools
import bisect
N = int(input())
L = list(map(int, input().split()))
ans = 0
LS = sorted(L)
l = len(LS)
for i in range(l):
  for j in range(l):
    if i < j:
      k = bisect.bisect_left(LS,LS[i]+LS[j])
      ans += k-j-1
print(ans)
