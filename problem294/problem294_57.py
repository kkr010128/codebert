import bisect
n=int(input())
l=sorted(list(map(int,input().split())))
ans=0
for i in range(n):
  for j in range(i+1,n):
    index=bisect.bisect_left(l,l[i]+l[j])
    ans+=index-j-1
print(ans)