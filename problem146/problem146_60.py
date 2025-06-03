import math
N=int(input())
A={}
mod=10**9+7
AZ,BZ,ZZ=0,0,0
for i in range(N):
  a,b=map(int, input().split())
  if a==b and a==0:
    ZZ+=1
  elif a==0:
    AZ+=1
    if (0,-1) not in A:
      A[(0,-1)]=1
    else:
      A[(0,-1)]+=1
  elif b==0:
    BZ+=1
    if (1,0) not in A:
      A[(1,0)]=1
    else:
      A[(1,0)]+=1
  else:
    if a<0:
      a*=-1
      b*=-1
    d=math.gcd(abs(a),abs(b))
    a//=d
    b//=d
    if (a,b) not in A:
      A[(a,b)]=1
    else:
      A[(a,b)]+=1
c=0
D=[]
for x,y in A:
  if (y,-x) in A:
    D.append((A[(x,y)],A[(y,-x)]))
    c+=A[(x,y)]+A[(y,-x)]
n=N-c-ZZ
p=pow(2,n,mod)
ans=p
for a,b in D:
  f=pow(2,a+b,mod)-(pow(2,a,mod)-1)*(pow(2,b,mod)-1)
  ans*=f
ans-=1
print((ans+ZZ)%mod)