while True:
    try:
        m,f,r = map(int,raw_input().split())
        if all(k == -1 for k in [m,f,r]):
            break
    except EOFError:
        break
    
    if m == -1 or f == -1:
        print 'F'
    elif m + f >= 80:
        print 'A'
    elif 65 <= m + f <80:
        print 'B'
    elif 50 <= m + f < 65:
        print 'C'
    elif 30 <= m + f < 50:
        if r >= 50:
            print 'C'
        else:
            print 'D'
    elif m + f < 30:
        print 'F'