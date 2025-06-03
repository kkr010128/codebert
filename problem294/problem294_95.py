import itertools
import bisect
n = int(input())
l = list(map(int,input().split()))
l.sort()
ans = 0

for i in range(len(l)-2):
  for j in range(i+1,len(l)):
    k = bisect.bisect_left(l, l[i]+l[j])
    if k > j:
      ans += k - j -1

print(ans)