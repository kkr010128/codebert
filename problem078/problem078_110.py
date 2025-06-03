n = int(input())
mod = 10**9+7

ans = 0
ans += pow(10, n, mod)
ans -= pow(9, n, mod)
ans -= pow(9, n, mod)
ans += pow(8, n, mod)

ans %= mod

print(ans)