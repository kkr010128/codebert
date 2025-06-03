n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(n):
  b.append(a[i]-(i+1))
  c.append(-(a[i]+i+1))
from collections import defaultdict
#cnt_b=Counter(b)
cnt_c=defaultdict(int)
ans=0
for i in range(n):
  v=cnt_c[b[i]]
  ans+=v
  cnt_c[c[i]]+=1
print(ans)