N=int(input())
A=[0]*N
ans=0
for i in range(1,N+1):
  ii=i
  while N>=ii:
    A[ii-1]+=1
    ii+=i
  ans+=A[i-1]*i
print(ans)