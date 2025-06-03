n, k = map(int, input().split())
l = [0 for i in range(k + 1)]
ans = 0
mod = 1000000007
for i in range(k, 0, -1):
    l[i] = pow(k // i, n, mod)
    tmp = 2 * i
    while tmp <= k:
        l[i] -= l[tmp]
        tmp += i
for i in range(k + 1):
    ans += i * l[i]
    ans %= mod
print(ans)