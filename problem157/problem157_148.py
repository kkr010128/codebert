from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))

memo = defaultdict(int)
ans = 0
for i, x in enumerate(a, 1):
    ans += memo[i - x]
    memo[x + i] += 1

print(ans)
