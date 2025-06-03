intInput = lambda: map(int, raw_input().split())
n, m, l = intInput()
A = [intInput() for _ in xrange(n)]
B = [intInput() for _ in xrange(m)]
for i in xrange(n):
    for j in xrange(l):
        print sum([A[i][k] * B[k][j] for k in xrange(m)]),
    print