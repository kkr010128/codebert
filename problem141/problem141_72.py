n,*l=map(int,open(0).read().split())
e=[1]
for i in range(n): e+=[(e[-1]-l[i])*2]
a=t=0
for i in range(n,-1,-1):
  if l[i]>e[i]: print(-1); break
  t=min(l[i]+t,e[i]); a+=t
else: print(a)