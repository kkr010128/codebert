n,d=map(int,input().split())
ans=0
for _ in range(n):
  x,y=map(int,input().split())
  dist=x**2+y**2
  dist=dist**(1/2)
  if dist<=d:
    ans+=1
print(ans)