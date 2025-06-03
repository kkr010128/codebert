n = int(input())
r = [int(input()) for _ in range(n)]

mi = r[0]
mx = -1e10
for j in range(1, len(r)):
    mx = max(mx, (r[j] - mi))
    mi = min(mi, r[j])
print(mx)