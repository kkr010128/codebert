h,w,K=map(int,input().split())
s=[list(input()) for i in range(h)]
from itertools import groupby
ans=10**18
for i in range(1<<h):
  pre=-1
  c=[]
  t_cnt=0
  op=[-1]*h
  for j in range(h):
    if i&(1<<j):op[j]=1
    else:op[j]=0
  gr=groupby(op)
  l=[]
  for key,g in gr:
    l.append(len(list(g)))
  c=[[0]*w for _ in range(len(l))]
  idx=0
  jdx=0
  for idx,li in enumerate(l):
    for k in range(li):
      for a in range(w):
        c[idx][a]+=int(s[jdx][a])
      jdx+=1
  # print(c)
  t_cnt=len(c)-1
  t_cnt1=0
  c_mx=[0]*len(c)
  ok=True
  for a in range(w):
    for b in range(len(c)):
      if c[b][a]>K:
        ok=False
      c_mx[b]+=c[b][a]
      if c_mx[b]>K:
        t_cnt1+=1
        c_mx=[0]*len(c)
        for b in range(len(c)):
          c_mx[b]+=c[b][a]
        break
  if ok:
    ans=min(ans,t_cnt+t_cnt1)
if ans==10**18:
  print(0)
else:
  print(ans)
