from itertools import accumulate
n, k = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(k):
    newa = [0 for _ in range(n)]
    for i in range(n):
        l = max(0, i - a[i])
        r = min(n - 1, i + a[i])
        newa[l] += 1
        if r + 1 < n:
            newa[r + 1] -= 1
    a = list(accumulate(newa))
    if all(i == n for i in a):
        break
print(*a)