
n=int(input())
l=list(map(int,input().split()))
from bisect import bisect_left
l.sort()

count=0
for a in range(n-2):
    for b in range(a+1,n-1):
        idx=bisect_left(l,l[a]+l[b],lo=b)
        count+=idx-(b+1)

print(count)