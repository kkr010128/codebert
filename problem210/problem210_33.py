f=input
n,s,q=int(f()),list(f()),int(f())
d={chr(97+i):[] for i in range(26)}
for i in range(n):
  d[s[i]]+=[i]
from bisect import *
for i in range(q):
  a,b,c=f().split()
  b=int(b)-1
  if a=='1':
    if s[b]==c: continue
    d[s[b]].pop(bisect(d[s[b]],b)-1)
    s[b]=c
    insort(d[c],b)
  else:
    t=0
    for l in d.values():
      m=bisect(l,b-1)
      if m<len(l) and l[m]<int(c): t+=1
    print(t)