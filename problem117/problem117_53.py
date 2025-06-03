n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=[0]
d=[0]

for i in range(n):
  c.append(c[-1]+a[i])
  
for j in range(m):
  d.append(d[-1]+b[j])

ans=0
for x in range(n+1):
  l=c[x]
  B=0
  if l<=k:
    h=k-l
    mi=0
    ma=m+1
    while ma-mi>1:
      mid=(mi+ma)//2
      if d[mid]<=h:
        mi=mid
      elif d[mid]>h:
        ma=mid
    B=mi
    
    ans=max(ans,x+B)
        
  
    
print(ans)
