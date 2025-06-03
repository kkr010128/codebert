n, m, k = map(int, input().split())
mod = 998244353

N = 10 ** 6


inv_t = [0]+[1]
for i in range(2, N):
    inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]


kai = [1, 1]
rev_kai = [1, inv_t[1]]
for i in range(2, N):
    kai.append(kai[-1] * i % mod)
    rev_kai.append(rev_kai[-1] * inv_t[i] % mod)


def cmb(n, r):
    return kai[n] * rev_kai[r] * rev_kai[n-r] % mod

base = m
ans = 0

for i in range(n-1):
    base = base * (m-1) % mod

for i in range(0, k+1):
    ans += base * cmb(n-1, n-1-i)
    ans %= mod
    base = base * inv_t[m-1] % mod

if m == 1 and k == n-1:
    print(1)
else:
    print(ans)
