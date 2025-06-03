from collections import Counter

N = int(input())
A = [int(_) for _ in input().split()]

cnt = Counter(A)

s = 0
for a in cnt:
    s += cnt[a] * (cnt[a] - 1) // 2

for a in A:
    print(s - cnt[a] + 1)
