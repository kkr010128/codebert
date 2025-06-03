#-------------------------------------------------------------------------------
# coding: utf-8
# Created:     16/12/2015
import sys

io = sys.stdin

while True:
    H, W = io.readline().split()
    h, w = int(H), int(W)
    if w==0 and h==0: break

    print "#"*w
    for x in xrange(h-2):
        print "#"+ "."*(w-2) + "#"

    print "#"*w
    print
pass