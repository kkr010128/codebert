while True:
    m, f, r = map(int, raw_input().split())

    if (m+f+r) == -3:
        break

    if (m * f) < 0:
        print "F"
    elif (m + f) >= 80:
        print 'A'
    elif 65 <= (m + f) < 80:
        print 'B'
    elif 50 <= (m + f) < 65:
        print 'C'
    elif 30 <= (m + f) < 50:
        if r < 50:
            print 'D'
        else:
            print 'C'
    elif (m + f) < 30:
        print 'F'