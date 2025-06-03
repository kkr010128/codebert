n = input()
for i in xrange(n):
    a, b, c = sorted(map(int, raw_input().split()))
    print 'YES' if a*a+b*b==c*c else 'NO'