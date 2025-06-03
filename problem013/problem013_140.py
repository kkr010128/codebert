n = input()
R = [input() for i in xrange(n)]
m = R[0]
ans = -1e10
for r in R[1:]:
    ans = max(ans, r - m)
    m = min(m, r)
print ans