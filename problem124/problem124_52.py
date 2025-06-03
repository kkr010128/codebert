MAXN = 2*10**6+2
p = 10**9 + 7

fact = [1] * MAXN
invfact = [1] * MAXN
for i in range(1, MAXN):
    fact[i] = fact[i-1] * i % p
invfact[MAXN-1] = pow(fact[MAXN-1], p-2, p)
for i in range(MAXN-1, 0, -1):
    invfact[i-1] = invfact[i] * i % p
    
def nCk(n, k):
    return fact[n] * invfact[n-k] * invfact[k] % p

K = int(input())
N = len(input())

ans = 0
for i in range(N, N+K+1):
    ans += pow(25, i-N, p) * nCk(i-1, N-1) * pow(26, N+K-i, p) % p
    ans %= p
print(ans)
