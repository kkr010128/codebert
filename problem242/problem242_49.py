n, k = map(int, input().split())
aa = list(map(int, input().split()))

aa.sort()
mod = 10 **9 +7
fac = [1] * 100000
inv = [1] * 100000
for i in range(1,len(fac)):
    fac[i] = fac[i-1] * i % mod
    inv[i] = pow(fac[i], mod-2, mod)
    
def combi(m, j):
    if j > m:
        return 0
    return (fac[m] * inv[m-j] * inv[j]) % mod


ret = 0
for i, a in enumerate(aa):
    n_max = combi(i, k-1)
    n_min = combi(n - 1 - i, k-1)
    ret = (ret + (n_max - n_min) * a) % mod
print(ret)