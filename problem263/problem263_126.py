n, *a = map(int, open(0).read().split())
mod = 10 ** 9 + 7
ans = 0
for i in range(60):
    cnt = 0
    for j in range(n):
        cnt += a[j] >> i & 1
    ans = (ans + (1 << i) * cnt * (n - cnt) % mod) % mod
print(ans)
