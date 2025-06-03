N, K = map(int, input().split())
ans = 0
lis = [0]*K
mod = 10**9 + 7

def modpow(a, n, mod):
    ans = 1
    while n > 0:
        if n&1:
            ans = ans * a % mod
        a = a * a % mod
        n = n >> 1
    return ans
for x in range(K,0, -1):
    a = int((K // x) % mod)
    b = modpow(a, N, mod)
    for i in range(2, K//x +1):
        b = (b - lis[x*i-1]) %mod
        if b < 0:
            b += mod
    lis[x-1] = b
    ans = (ans + b*x%mod) % mod
print(int(ans))
