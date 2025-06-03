from collections import Counter

N = int(input())
A = tuple(map(int, input().split(' ')))

counter = Counter(A)

patterns = 0
for value in counter.values():
    if value >= 2:
        patterns += value * (value - 1) // 2

for a in A:
    ans = patterns
    if counter[a] >= 2:
        ans -= counter[a] * (counter[a] - 1) // 2
    if counter[a] >= 3:
        ans += (counter[a] - 1) * (counter[a] - 2) // 2
    print(ans)
