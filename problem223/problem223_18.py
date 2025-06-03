from itertools import accumulate
N, K = map(int, input().split())
P = list(map(int, input().split()))
acc = [0] + list(accumulate(P))
ans = 0
for a, b in zip(acc, acc[K:]):
  exp = (b - a + K) / 2
  ans = max(exp, ans)
print(ans)