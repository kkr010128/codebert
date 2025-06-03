n = int(input())
mod = 1000000007


def _mod(x, y):
    res = 1
    for i in range(y):
        res = (res * x) % mod
    return res


ans = _mod(10, n) - _mod(9, n) - _mod(9, n) + _mod(8, n)
ans %= mod
ans = (ans + mod) % mod
print(ans)
