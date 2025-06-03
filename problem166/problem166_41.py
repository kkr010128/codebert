s=input()
n=len(s)

from collections import Counter
c=Counter()
m=0
c[m]+=1
d=1
s=s[::-1]
for i in range(n):
  m+=int(s[i])*d
  m%=2019
  d*=10
  d%=2019
  c[m]+=1
ans=0
for v in c.values():
  ans+=v*(v-1)//2
print(ans)
