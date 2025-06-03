from collections import defaultdict

N, *A = map(int, open(0).read().split())

ctr1 = defaultdict(int)
ctr2 = defaultdict(int)
for i in range(N):
    ctr2[i + A[i]] += 1
    if i - A[i] > 0:
        ctr1[i - A[i]] += 1

ans = 0
for v in ctr1:
    ans += ctr1[v] * ctr2[v]
print(ans)
