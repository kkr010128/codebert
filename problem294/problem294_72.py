N=int(input())
L=list(map(int,input().split()))
L.sort()
from bisect import bisect_left
ans = 0
for i1 in range(N-2):
  for i2 in range(i1+1,N-1):
    l1,l2 = L[i1],L[i2]
    #th = bisect_left(L[i2+1:],l1+l2)
    #print(l1,l2,L[i2+1:],(l2-l1+1)*(-1),th)
    th = bisect_left(L,l1+l2)
    ans += max(th-i2-1,0)
print(ans)