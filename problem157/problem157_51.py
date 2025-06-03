n=int(input())
a=list(map(int,input().split()))
ans=0

plus=[0]*1000000
minus=[0]*1000000

for i in range(n):
  ene=i+1
  pin=a[i]
  pl,mi=ene+pin,ene-pin
  if 0<=pl<1000000:
    plus[pl]+=1
  if 0<=mi<1000000:
    minus[mi]+=1
  
for i in range(1000000):
  ans+=plus[i]*minus[i]
  

print(ans)