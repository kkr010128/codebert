n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7

factorial = [1]
inverse = [1]
for i in range(1, n+1):
    factorial.append(factorial[-1] * i % mod)
    inverse.append(pow(factorial[-1], mod - 2, mod))

def comb(n, r, mod):
    if n < r or r < 0: return 0
    elif r == 0: return 1
    return factorial[n] * inverse[r] * inverse[n - r] % mod

a.sort()
mini = 0
for i in range(n-1):
    mini += a[i] * comb(n-i-1, k-1, mod)
    mini %= mod

a.sort(reverse=True)
maxi = 0
for i in range(n-1):
    maxi += a[i] * comb(n-i-1, k-1, mod)
    maxi %= mod

print((maxi-mini)%mod)