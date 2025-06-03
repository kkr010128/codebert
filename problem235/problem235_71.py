from collections import defaultdict

def prime_factors(n):
    d = defaultdict(int)
    while n%2 == 0:
        d[2] += 1
        n //= 2
    i = 3
    while i*i <= n:
        while n%i == 0:
            d[i] += 1
            n //= i
        i += 2
    if n > 2:
        d[n] += 1
    return d

MOD = 10**9+7
N = int(input())
A = list(map(int, input().split()))
G = defaultdict(int)
for a in A:
    pf = prime_factors(a)
    for k,v in pf.items():
        G[k] = max(G[k], v)
lcm = 1
for k,v in G.items():
    lcm *= pow(k, v, MOD)
    lcm %= MOD
ans = 0
for a in A:
    ans += lcm * pow(a, MOD-2, MOD) % MOD
    ans %= MOD
print(ans)