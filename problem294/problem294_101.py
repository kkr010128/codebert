import itertools
import bisect

N = int(input())
LS = list(map(int,input().split()))
LS.sort()

ans = 0

for a,b in itertools.combinations(LS,2):
  a,b = min(a,b),max(a,b)
  lo = b - a
  up = a + b
  
  cnt = bisect.bisect_left(LS,up) - bisect.bisect_right(LS,lo) - 1
  if lo < a:
    cnt -= 1
    
  if cnt <= 0:
    continue
    
  ans += cnt
  
print(ans // 3)

