import collections
import sys

input = sys.stdin.readline

ri = lambda: int(input())
rs = lambda: input().rstrip()
ril = lambda: list(map(int, input().split()))
rsl = lambda: input().rstrip().split()
ris = lambda n: [ri() for _ in range(n)]
rss = lambda n: [rs() for _ in range(n)]
rils = lambda n: [ril() for _ in range(n)]
rsls = lambda n: [rsl() for _ in range(n)]

n, k = ril()
ls = ril()
acc = [0]
for x in ls:
    acc.append((acc[-1] + x - 1) % k)
counter = collections.Counter(acc[:k])
res = 0
for i in range(n + 1):
    res += counter[acc[i]] - 1
    counter[acc[i]] -= 1
    if i + k < n + 1:
        counter[acc[i + k]] += 1
print(res)