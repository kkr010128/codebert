n, m, l = map(int, raw_input().split())
A = [map(int, raw_input().split()) for i in xrange(n)]
B = [map(int, raw_input().split()) for i in xrange(m)]
C = [[0] * l for i in xrange(n)]

for i in xrange(n):
    for j in xrange(l):
        C[i][j] = sum(A[i][k] * B[k][j] for k in xrange(m))
for c in C:
    print " ".join(map(str, c))