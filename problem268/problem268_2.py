from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

Count = {x:0 for x in range(0, n)}

mod = 10**9+7
ans = 1

for i in range(n):
    now = A[i]
    if now == 0:
        ans = (3 - Count[0]) * ans % mod
        Count[0] += 1
        continue
    ans = (Count[now-1] - Count[now]) *ans  % mod
    Count[now] += 1

print(ans)
# print(Count)