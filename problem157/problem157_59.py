
from collections import defaultdict

N = int(input())
X = list(map(int, input().split()))

ctr = defaultdict(int)
ans = 0
for i in range(N):
    ctr[i + X[i]] += 1
    ans += ctr[i - X[i]]

print(ans)
