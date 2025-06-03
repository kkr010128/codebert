N=int(input())
A=list(map(int,input().split()))
mod = 10**9+7
x,y,z=0,0,0
ans=1
for a in A:
  ans*=[x,y,z].count(a)
  ans%=mod
  if x==a:
    x+=1
  elif y==a:
    y+=1
  else:
    z+=1
print(ans)