MOD = int(1e9) + 7
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(60):
    cnt = 0
    for j in range(n):
        if a[j] >> i & 1 == 1:
            cnt += 1
    ans += (cnt * (n-cnt) * (2**i)) % MOD
ans %= MOD
print(ans)
