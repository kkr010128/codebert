N, K = map(int,input().split())
mod = 10**9+7
gcd_num = [1]*(K+1)
for i in range(K//2, 0, -1):
    gcd_num[i] = pow((K//i), N, mod)
    for j in range(2, K//i + 1):
        gcd_num[i] -= gcd_num[i*j]
    gcd_num[i] = gcd_num[i]%mod
ans = 0
for i in range(1,K+1):
    ans += i * gcd_num[i] % mod
print(ans%mod)