N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict, Counter

counted_a = Counter(A)
total = 0

for key, v in counted_a.items():
    total += v * (v-1) // 2

ans = []
for a in A:
    v = counted_a[a]
    t = total - v * (v-1) // 2 + (v-1) * (v-2) // 2
    ans.append(t)

print(*ans, sep='\n')