n,k=map(int,input().split())
m=10**9+7

k=min(k,n-1)
t,c,h=1,1,1
for i in range(1,k+1):
  p=pow(i,m-2,m)
  c=(c*(n-i+1)* p)%m
  h=(h*(n-i)  * p)%m
  t=(t+c*h)%m

print(t%m)
