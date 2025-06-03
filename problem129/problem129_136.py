from collections import Counter
N = int(input())
A = list(map(int, input().split()))
A.sort()
A_max = A[-1]
dp = [1]*(A_max+1)
# dp[i] = 1: iはAのどの要素の倍数でもない
# dp[i] = 0: iはAの要素の倍数である
for a in A:
    if not dp[a]:
        continue
    y = a*2
    while y <= A_max:
        dp[y] = 0
        y += a
# Aの要素それぞれについて、dp[a] = 1ならよいが
# Aの要素ai,ajでai=ajとなる場合、上の篩では通過しているのに
# 条件を満たさない
cnt = dict(Counter(A))
ans = 0
for a in A:
    if cnt[a] >= 2:
        continue
    if dp[a]:
        ans += 1
print(ans)