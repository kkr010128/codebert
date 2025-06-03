MOD = 10**9+7
n = int(input())
a = list(map(int, input().split()))
cnt = [0 for _ in range(n)]
ans = 1
for x in a:
    if x > 0:
        ans *= cnt[x-1] - cnt[x]
    else:
        ans *= 3 - cnt[0]
    cnt[x] += 1
    ans %= MOD
print(ans)
