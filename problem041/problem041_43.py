# -*- coding: utf-8 -*-

list = map(int, raw_input().split())
W = list[0]
H = list[1]
x = list[2]
y = list[3]
r = list[4]

if (x-r) >= 0 and (y-r) >= 0 and (x+r) <= W and (y+r) <= H:
    print "Yes"
else:
    print "No"