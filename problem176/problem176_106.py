mod=10**9+7
n,k=map(int,input().split())
cnt=[0]*k
for i in range(k,0,-1):
	cnt[i-1]=pow(k//i,n,mod)
	for j in range(i*2,k+1,i):
		cnt[i-1]-=cnt[j-1]
	cnt[i-1]%=mod
ans=0
for i in range(k):
	ans+=cnt[i]*(i+1)%mod
print(ans%mod)