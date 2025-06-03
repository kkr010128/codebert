n = input()

for i in xrange(n):
    tmp = map(int, raw_input().split())
    if tmp[0]**2 + tmp[1]**2 == tmp[2]**2 or tmp[1]**2 + tmp[2]**2 == tmp[0]**2 or tmp[2]**2 + tmp[0]**2 == tmp[1]**2:
        print "YES"
    else:
        print "NO"