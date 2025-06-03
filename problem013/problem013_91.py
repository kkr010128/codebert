n = input()
maxv = - 1 * pow(10, 9)
minv = input()
for _ in xrange(1, n):
    Rj = input()
    maxv = max(maxv, Rj - minv)
    minv = min(minv, Rj)

print maxv