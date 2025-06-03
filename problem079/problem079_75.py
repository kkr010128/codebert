s=int(input())
a=1
mod=10**9+7
x=s//3
y=s%3
ans=0
while x>=1:
  xx=1
  for i in range(1,x):
    xx*=i
    xx%=mod
  yy=1
  for j in range(1,1+y):
    yy*=j
    yy%=mod
  fx=pow(xx,mod-2,mod)
  fy=pow(yy,mod-2,mod)
  xxyy=1
  for k in range(1,x+y):
    xxyy*=k
    xxyy%=mod
  ans+=(xxyy*fx*fy)%mod
  x-=1
  y+=3
print(ans%mod)