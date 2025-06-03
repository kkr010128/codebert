from collections import defaultdict
MOD = 10**9+7
n = int(input())
A = list(map(int, input().split()))


def sieve(n):
    n += 1
    res = [i for i in range(n)]
    for i in range(2, int(n**.5)+1):
        if res[i] < i:
            continue
        for j in range(i**2, n, i):
            if res[j] == j:
                res[j] = i
    return res


U = max(A)+1
min_factor = sieve(U)


def prime_factor(n):
    res = defaultdict(lambda: 0)
    while 1 < n:
        res[min_factor[n]] += 1
        n //= min_factor[n]
    return res


pf = defaultdict(lambda: 0)

for a in A:
    for p, q in prime_factor(a).items():
        if pf[p] < q:
            pf[p] = q

x = 1
for p, q in pf.items():
    x *= pow(p, q, MOD)
x %= MOD

print(sum(x*pow(a, MOD-2, MOD) for a in A) % MOD)