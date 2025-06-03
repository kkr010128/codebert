MOD = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(60):
    cnt = 0
    for x in a:
        if (x >> i) & 1:
            cnt += 1
    ans += cnt * (n - cnt) * (1 << i)
print(ans % MOD)
