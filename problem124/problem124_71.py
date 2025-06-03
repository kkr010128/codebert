k = int(input())
s = input()
n = len(s)
mod = 10 ** 9 + 7

f = [1, 1]
f_inv = [1, 1]
inv = [0, 1]
 
for i in range(2, n+k+1):
    f.append((f[-1] * i ) % mod)
    inv.append((-inv[mod % i] * (mod // i) ) % mod)
    f_inv.append((f_inv[-1] * inv[-1]) % mod)

def comb(n, k):
    return f[n] * f_inv[k] * f_inv[n-k] % mod

ans = 0
for i in range(k+1):
    x = pow(25, i, mod) * pow(26, k-i, mod) * comb(n-1+i, n-1)
    ans += x
    ans %= mod

print(ans)