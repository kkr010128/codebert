s=int(input())
a=[0]*(s+1)
a[0]=1
mod=10**9+7
for i in range(3,s+1):
    a[i]=a[i-3]+a[i-1]
print(a[s]%mod)
