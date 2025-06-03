import sys
import math

H, W = map(int, raw_input().split())

while H > 0 or W > 0 :
    for y in xrange(H) :
        for x in xrange(W) :
            if (x + y) % 2 == 0 :
                sys.stdout.write("#")
            else :
                sys.stdout.write(".")

        print
    print

    H, W = map(int, raw_input().split())