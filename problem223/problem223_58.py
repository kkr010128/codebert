n, k = map(int, input().split())
lp = list(map(int, input().split()))

le = [(p + 1) / 2 for p in lp]

e = sum(le[:k])
m = e
for i in range(n - k):
    e -= le[i]
    e += le[k + i]
    m = max(m, e)

print(m)
