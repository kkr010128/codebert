import math

H, W = map(int, raw_input().split())

while H > 0 or W > 0 :
    print "#" * W

    for i in xrange(H-2) :
        print "#" + "." * (W-2) + "#"

    print "#" * W
    print

    H, W = map(int, raw_input().split())