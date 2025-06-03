while True:
    i,e,r = map(int,raw_input().split())

    if i == e == r == -1:
        break
    if i == -1 or e == -1 :
        print 'F'
    elif i+e >= 80 :
        print 'A'
    elif i+e >= 65 :
        print 'B'
    elif i+e >= 50 :
        print 'C'
    elif i+e >= 30 :
        if r >= 50 :
            print 'C'
        else :
            print 'D'
    else :
        print 'F'