import sys
import collections
s=sys.stdin.readlines()
n,q=map(int,s[0].split())
d=collections.deque(e.split()for e in s[1:])
t=0
while d:
 k,v=d.popleft()
 v=int(v)
 if v>q:
  v-=q
  t+=q
  d.append([k,v])
 else:
  t+=v
  print(k,t)
