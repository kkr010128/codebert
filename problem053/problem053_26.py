n = input()
m = map(int, raw_input().split())
m2 = [0 for i in xrange(n)]

for i in xrange(n):
    m2[n-i-1] = m[i]

for i in xrange(n):
    print m2[i],