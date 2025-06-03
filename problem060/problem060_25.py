import sys
import math

n, m, l = map(int, raw_input().split())

A = [[0 for i in xrange(m)] for j in xrange(n)]
B = [[0 for i in xrange(l)] for j in xrange(m)]

for i in xrange(n):
    A[i] = map(int, raw_input().split())

for i in xrange(m):
    B[i] = map(int, raw_input().split())

for i in xrange(n):
    for j in xrange(l):
        sm = 0
        for k in xrange(m):
            sm += A[i][k] * B[k][j]

        sys.stdout.write(str(sm))
        if j < l-1:
            sys.stdout.write(" ")
    print