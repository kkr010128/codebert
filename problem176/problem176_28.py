n,k=map(int,input().split())
cnt=[0]*(k+1)
mod=10**9+7
for i in range(1,k+1):
  cnt[i]=pow(k//i,n,mod)
#print(cnt)
for i in range(k):
  baisu=k//(k-i)
  for j in range(2,baisu+1):
    cnt[k-i]=(cnt[k-i]-cnt[(k-i)*j]+mod)%mod
ans=0
for i in range(1,k+1):
  ans+=i*cnt[i]
  ans%=mod
print(ans)