
from collections import Counter

N = int(input())
X = list(map(int, input().split()))
ctr = Counter(X)

ans = 0
for v in ctr.values():
    ans += v * (v - 1) // 2

for i in range(N):
    val = ctr[X[i]]
    print(ans - val * (val - 1) // 2 + (val - 1) * (val - 2) // 2)
