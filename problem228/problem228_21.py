h=int(input())
res=1
ans=0
while h>1:
  h=int(h/2)
  ans+=res
  res*=2
print(ans+res)