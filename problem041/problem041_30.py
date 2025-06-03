#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def judge(W, H, x, y, r):
    if (x - r) >= 0 and (y - r) >= 0 and\
       (x + r) <= W and (y + r) <= H:
        print "Yes"
    else:
        print "No"

W, H, x, y, r = map(int, raw_input().split())

if -100 <= x <= 100 and -100 <= y <= 100 and \
   0 < W <= 100 and 0 < H <= 100 and 0 < r <= 100:
    judge(W, H, x, y, r)
else:
    print "error!!"
    sys.exit(0)