from collections import Counter
def mpow(a,b,mod):
  ret=1
  while b>0:
    if b&1:
      ret=(ret*a)%mod
    a=(a*a)%mod
    b>>=1
  return ret
n,p=map(int,input().split())
s=[int(i) for i in input()]
if p==2 or p==5:
  ans=0
  for i in range(n):
    if s[i]%p==0:
      ans+=i+1
  print(ans)
else:
  ans=0
  d=Counter()
  d[0]+=1
  num=0
  for i in range(n-1,-1,-1):
    num=(num+s[i]*mpow(10,n-1-i,p))%p
    ans+=d[num]
    d[num]+=1
  print(ans)




