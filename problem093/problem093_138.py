INF=10**9
f=lambda:[*map(int,input().split())]
n,k=f()
p,c=f(),f()
p=[*map(lambda x:x-1,p)]
tp=[[*range(n)] for _ in range(n+1)]
tc=[[0]*n for _ in range(n+1)]
lt=[0]*n
lc=[0]*n
for i in range(n):
  for j in range(n):
    t=p[tp[i][j]]
    tp[i+1][j]=t
    tc[i+1][j]=tc[i][j]+c[t]
    if t==j and lt[j]==0:
      lt[j]=i+1
      lc[j]=tc[i+1][j]
a=-INF
for i in range(n):
  if lc[i]<1 or k<=lt[i]:
    for j in range(min(lt[i],k)):
      a=max(a,tc[j+1][i])
  else:
    for j in range(lt[i]):
      t=k//lt[i]*lc[i]+tc[j+1][i]
      if k%lt[i]<j+1: t-=lc[i]
      a=max(a,t)
print(a)