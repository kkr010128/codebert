a, b = map(int, raw_input().split())

for i in xrange(10000) :

    print str(min(a, b)) + ' ' + str(max(a, b))

    a, b = map(int, raw_input().split())

    if a == 0 and b == 0 :
        break