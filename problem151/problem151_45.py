n, m, k = map(int, input().split())

mod = 998244353

def _fac_inv(_n, _mod):
    _fac = [1] * (_n+1)  # 階乗
    _inv = [1] * (_n+1)  # 逆元
    for i in range(_n):
        _fac[i+1] = _fac[i] * (i+1) % _mod
    _inv[n] = pow(_fac[n], mod-2, mod)
    for i in range(_n, 0, -1):
        _inv[i-1] = _inv[i] * i % _mod

    return _fac, _inv

fac, inv = _fac_inv(n, mod)

ans = 0
mm = (m * pow(m-1, n-1-k, mod)) % mod
for ii in range(k+1):
    i = k-ii
    ans = (ans + mm * fac[n-1] * inv[i] * inv[n-1-i]) % mod
    mm = mm * (m-1) % mod

print(ans)
