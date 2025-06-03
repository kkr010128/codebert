def aizu001 ():
    xs = map(int,raw_input().split())
    a = xs[0]
    b = xs[1]
    if a > b:
        print "a > b"
    elif a < b:
        print "a < b"
    else :
        print "a == b"

aizu001()