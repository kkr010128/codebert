import bisect
n=int(input())
l=sorted(list(map(int,input().split())))
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        index=bisect.bisect_left(l,l[i]+l[j])
        if j<index:
            ans+=index-j-1
print(ans)