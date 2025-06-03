n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7
b = 1
ans = 0
for i in range(k - 1, n):
    ans += b * (a[i] - a[n - i - 1])
    ans %= mod
    b = (i+1)*pow(i-k+2, mod - 2, mod) * b % mod
print(ans)