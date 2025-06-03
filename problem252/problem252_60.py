n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

import bisect 

def func(x):
  C = 0
  for p in l:
    q = x -p
    j = bisect.bisect_left(l, q)
    C += n-j
  if C >= m:
    return True
  else:
    return False
  
l_ = 0
r_ = 2*10**5 +1
while l_+1 < r_:
  c_ = (l_+r_)//2
  if func(c_):
    l_ = c_
  else:
    r_ = c_
    
ans = 0
cnt = 0
lr = sorted(l, reverse=True)
from itertools import accumulate
cum = [0] + list(accumulate(lr))
for i in lr:
  j = bisect.bisect_left(l, l_-i)
  ans += i*(n-j) + cum[n-j]
  cnt += n -j
ans -= (cnt-m)*l_
print(ans)