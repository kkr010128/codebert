from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
d=defaultdict(int)
x=[i+1+a[i] for i in range(n)]
y=[i+1-a[i] for i in range(n)]
for i in range(n):
    d[i+1-a[i]]+=1
ans=0
for i in range(n):
    ans+=d[i+1+a[i]]
print(sum(d[i+1+a[i]] for i in range(n)))