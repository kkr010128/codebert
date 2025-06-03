import bisect
n,m=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
ng=-1
ok=A[-1]*2+1
B=[[0]*n for k in range(2)]
ii=0
while ok-ng>1:
  mid=(ok+ng)//2
  d=0
  for i in range(n):
    c=n-bisect.bisect_right(A,mid-A[i],lo=0,hi=len(A))
    B[ii][i]=c
    d=d+c
  if d<m:
    ok=mid
    ii=(ii+1)%2
  else:
    ng=mid
D=[0]
for i in range(n):
  D.append(D[-1]+A[n-i-1])
ans=0
for i in range(n):
  x=B[(ii+1)%2][i]
  ans=ans+A[i]*x+D[x]
ans=ans+(m-sum(B[(ii+1)%2]))*ok
print(ans)