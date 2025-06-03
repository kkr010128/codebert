n = int(input())
r = []
for _ in range(n):
    r.append(int(input()))

maxv = -2 * 10**9
minv = r[0]

for ri in r[1:]:
    maxv = max(maxv, ri - minv)
    minv = min(minv, ri)

print(maxv)
