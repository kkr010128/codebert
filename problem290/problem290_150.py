n,k=map(int,input().split())
a=list(map(int,input().split()))
f=list(map(int,input().split()))
a.sort()
f.sort()
f.reverse()
l=-1;r=max(a)*max(f)+1
sum=sum(a)
while abs(l-r)>1:
  x=(l+r)//2
  ct=0
  for i in range(n):
    ct+=max(a[i]-(x//f[i]),0)
  if ct<=k:
    r=x
  else:
    l=x
print(r)