def pre_c(n, mod):
    f = [0] * (n + 1)
    g = [0] * (n + 1)
    for i in range(n + 1):
        if i == 0:
            f[i] = 1
            g[i] = 1
        else:
            f[i] = (f[i - 1] * i) % mod
            g[i] = pow(f[i], mod - 2, mod)

    return f, g

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
mod = 10 ** 9 + 7
f, g = pre_c(n, mod)

ans = 0
for i in range(n - k + 1):
    min_temp = a[i] * f[n - i - 1] * g[k - 1] * g[n - i - 1 - k + 1] % mod
    max_temp = a[n - i - 1] * f[n - i - 1] * g[k - 1] * g[n - i - 1 - k + 1] % mod

    ans = (ans + (max_temp - min_temp) % mod ) %mod
print(ans)
