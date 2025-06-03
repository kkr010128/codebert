x, y  = map(int, input().split())
mod = 10 ** 9 + 7
if (x + y) % 3 != 0:
    ans = 0
else:
    n, m = (2 * x - y) / 3, (2 * y - x) / 3
    ans = 0
    if n >= 0 and m >= 0:
        n, m = int(n), int(m)
        ans = 1
        for i in range(min(m, n)):
            ans = ans * (n + m - i) % mod 
            ans *= pow(i + 1, mod - 2, mod)

print(ans % mod)