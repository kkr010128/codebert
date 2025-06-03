from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
d=defaultdict(int)
for i in range(n):
    d[i-a[i]]+=1
ans=0
for i in range(n):
    ans+=d[i+a[i]]
print(ans)