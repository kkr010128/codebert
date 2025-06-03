import bisect
n=int(input())
l=[int(x) for x in input().rstrip().split()]
l.sort()

ans=0
comb=[]
ans=0
for i in range(n):
    for j in range(i+1,n):
        now=l[i]+l[j]
        ind=bisect.bisect_left(l,now)
        ans+=max(0,ind-j-1)

print(ans)
