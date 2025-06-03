import sys
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
MOD=10**9+7
plus=[]
minus=[]
zero=[]
for i in range(n):
  if a[i]>0:
    plus.append(a[i])
  if a[i]<0:
    minus.append(a[i])
  if a[i]==0:
    zero.append(a[i])
if k==n:
  ans=1
  for i in range(k):
    ans=(ans*a[i])%MOD
  print(ans)
  sys.exit()
if len(plus)==0:
  if k%2!=0:
    a.reverse()
  ans=1
  for i in range(k):
    ans=(ans*a[i])%MOD
  print(ans)
  sys.exit()
if len(plus)+len(minus)<k:
  print(0)
  sys.exit()
m=len(minus)
minus.sort()
plus.reverse()
plpointer=k
if k>len(plus):
  plpointer=2*(len(plus)//2)
  if k%2==1:
    if plpointer+1<=len(plus):
      plpointer+=1
    else:
      plpointer-=1
mnpointer=k-plpointer
while mnpointer<m-1 and plpointer>=2 and minus[mnpointer]*minus[mnpointer+1]>plus[plpointer-1]*plus[plpointer-2]:
  mnpointer+=2
  plpointer-=2
ans=1
for i in range(mnpointer):
  ans=(ans*minus[i])%MOD
for i in range(plpointer):
  ans=(ans*plus[i])%MOD
print(ans)
