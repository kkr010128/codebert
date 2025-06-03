mod = pow(10, 9) + 7
def powmod(x, y):
    res = 1
    for i in range(y):
        res = res * x % mod
    return res

n = int(input())
ans = powmod(10, n) - powmod(9, n) - powmod(9, n) + powmod(8, n)
ans %= mod
ans = (ans + mod) % mod
print(ans)
