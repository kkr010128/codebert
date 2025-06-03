"""
i - j = A[i] + A[j]
> i - A[i] = j + A[j]
i > j
"""
from collections import defaultdict

N = int(input())
high = list(map(int, input().split()))

ans = 0
calc = defaultdict(int)
for i in range(1, N+1):
  ans += calc[i - high[i-1]]
  calc[i + high[i-1]] += 1

print(ans)