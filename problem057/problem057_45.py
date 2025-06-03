

n = 0
while n == 0:
    m = map(int,raw_input().split())
    if m[0] + m[1] + m[2] == -3:
        break
    if m[0] == -1 or m[1] == -1:
        print "F"
    else:
        for i in xrange(2):
            if m[i] == -1:
                m[i] = 0
        k = m[0] + m[1]
        if k >= 80:
            print "A"
        elif k >= 65:
            print "B"
        elif k >= 50:
            print "C"
        elif k >= 30:
            if m[2] >= 50:
                print "C"
            else:
                print "D"
        elif k < 30:
            print "F"