n = int(input())
l = list(map(int,input().split()))

from itertools import accumulate
cum=list(accumulate(l))

tot=sum(l)
ans=2020202020*100000
for i in cum:
    ans=min(ans, abs(tot-i*2))
print(ans)
