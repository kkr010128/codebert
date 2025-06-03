from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
found = 0
dt = defaultdict(int)
for n in range(N):
    found += dt[n - A[n]]
    dt[n + A[n]] += 1
print(found)