n = int(input())
a = [0,0,0]
mod = 1000000007
su=0
for i in range(3,n+1):
    su=(su+a[i-3])%mod
    a.append((su+1)%mod)
print(a[n])