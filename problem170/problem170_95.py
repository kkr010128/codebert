n, k = map(int, input().split())
MOD = 10 ** 9 + 7
ans = 0

for i in range(k, n + 2):
    mini = i * (i - 1) / 2
    maxx = i * (2 * n - i + 1) / 2

    ans += maxx - mini + 1
    ans %= MOD

print(int(ans))
