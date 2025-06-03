while True:
    h,w = map(int,raw_input().split())
    if h==0 and w==0:
        break
    sside="" #square side
    inside=""
    for x in xrange(1,w+1):
        sside += "#"
        if x==1 or x==w:
            inside += "#"
        else:
            inside += "."
    for x in xrange(1,h+1):
        if x==1 or x==h:
            print sside
        else:
            print inside
    print