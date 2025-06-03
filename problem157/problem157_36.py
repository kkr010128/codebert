from collections import defaultdict
import bisect
def f():
    return []

d=defaultdict(f)
n=int(input())
a=list(map(int,input().split()))
x=[i+1+a[i] for i in range(n)]
y=[i+1-a[i] for i in range(n)]
for i in range(n):
    d[y[i]].append(i)

ans=0
for i in range(n):
    ans+=len(d[x[i]])
print(ans)