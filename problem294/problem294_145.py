import sys
import bisect
N = int(input())
L = list(map(int, input().split()))
LS = sorted(L)
ans = 0
for i in range(N):
  for j in range(N):
    if i < j:
      index = bisect.bisect_left(LS,LS[i]+LS[j])
      ans += index-j-1 

print(ans)