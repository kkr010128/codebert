f=lambda:[*map(int,input().split())]
n,k=f()
p,c=f(),f()
p=[i-1 for i in p]
a=-10**9
for i in range(n):
  x,l,s,t=i,[],0,0
  while 1:
    x=p[x]
    l+=[c[x]]
    s+=c[x]
    if x==i: break
  m=len(l)
  for j in range(m):
    if j+1>k: break
    t+=l[j]
    a=max(a,t+(k-j-1)//m*s*(s>0))
print(a)