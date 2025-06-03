N=int(input())
A=list(map(int,input().split()))
def f(x):
  if x==1:
    return dict()
  y=x
  r=dict()
  for i in range(2,int(x**0.5)+1):
    if y%i==0:
      r[i]=0
      while y%i==0:
        r[i]+=1
        y=y//i
    if y==1:
      break
  if y!=1:
    r[y]=1
  return r

B=[f(A[i]) for i in range(N)]
def g(X):
  if len(X)==1:
    return X[0]
  a,b=g(X[:len(X)//2]),g(X[len(X)//2:])
  c=list(set(a.keys())|set(b.keys()))
  for i in range(len(c)):
    a[c[i]]=max(a.get(c[i],0),b.get(c[i],0))
  return a

G=g(B)
X=1
mod=10**9+7
P=0
Y=list(G.keys())
for i in range(len(Y)):
  X=X*pow(Y[i],G[Y[i]],mod)%mod
for i in range(N):
  P=(P+X*pow(A[i],mod-2,mod))%mod
print(P)