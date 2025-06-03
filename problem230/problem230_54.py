from bisect import bisect_right
N,D,A=map(int,input().split())
X,H=[None]*N,{}
for i in range(N):
  X[i],H[X[i]]=map(int,input().split())
X.sort()
f=[0]*N
ans=i=0
while i<N:
  if i>0:
    f[i]+=f[i-1]
  if f[i]*A<H[X[i]]:
    k=-((f[i]*A-H[X[i]])//A)
    f[i]+=k
    ans+=k
    j=bisect_right(X,X[i]+(D<<1))
    if j<N:
      f[j]-=k
  i+=1
print(ans)