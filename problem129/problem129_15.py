# ABC170

n = int(input())
a = list(map(int, input().split()))

a.sort()
a_max = max(a)
dp = [True for _ in range(a_max+1)]

ans = 0
for i in range(n):
    if dp[a[i]]:
        for j in range(0, a_max+1, a[i]):
            dp[j] = False
        if i > 0:
            if a[i] == a[i-1]:
                continue
        if i < n-1:
            if a[i] == a[i+1]:
                continue
        ans += 1

print(ans)
