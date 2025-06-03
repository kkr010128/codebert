n = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

ans = 0

for i in range(61):
    cnt0 = 0
    cnt1 = 0
    for a in A:
        if (a>>i) & 1 == 0:
            cnt0 += 1
        else:
            cnt1 += 1
    ans += cnt0 * cnt1 * (2 ** i)
    ans %= mod

print(ans)