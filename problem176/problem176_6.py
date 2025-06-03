N, K = map(int, input().split())
mod = 10**9+7
gcd_l = [0]*K

for i in range(K, 0, -1):
    n = pow((K//i), N, mod)
    for x in range(i, K+1, i):
        n -= gcd_l[K-x]
    gcd_l[K-i] = n%mod

res = 0
for i in range(K):
    res += (gcd_l[i] * (K-i))%mod

print(res%mod)