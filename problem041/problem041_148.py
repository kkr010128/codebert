def aizu004():
    xs = map(int,raw_input().split())
    W = xs[0]
    H = xs[1]
    x = xs[2]
    y = xs[3]
    r = xs[4]
    if (r <= x <= W-r) and (r <= y <= H-r):
        print "Yes"
    else:
        print "No"
aizu004()