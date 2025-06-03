a,b  = map(int, raw_input().split())
A = [map(int, raw_input().split()) for _ in xrange(a)]
B = [input() for _ in xrange(b)]
C = [sum([A[i][j] * B[j] for j in xrange(b)]) for i in xrange(a)]
for x in C:
    print x