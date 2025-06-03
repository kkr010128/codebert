MOD=10**9+7
n, k = map(int, input().strip().split())
d=[0]*(k+1)
d[0]=None

for i in range(1,k+1):
    d[i]=pow(k//i,n,MOD)

# update d
for i in range(k,0,-1):
    for j in range(i*2,k+1,i):
        d[i]-=d[j]
        d[i]%=MOD
ans=0
for i in range(1,k+1):
    ans+=d[i]*i%MOD
    ans%=MOD
print(ans)