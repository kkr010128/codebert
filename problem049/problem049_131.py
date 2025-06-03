while True:
    H,W = map(int,raw_input().split())
    if H == 0 and W == 0:
        break
    a = "#"
    for i in xrange(0,H):
        print a * W
    print ""