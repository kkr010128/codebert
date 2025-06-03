#-------------------------------------------------------------------------------
# coding: utf-8
# Created:     16/12/2015

import sys
io = sys.stdin

while True:
    arr = io.readline().split()
    h, w = int(arr[0]), int(arr[1])
    if h==0 and w ==0 : break

    for x in xrange(h):
        print "#"*w
    print

pass