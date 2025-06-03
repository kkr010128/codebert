# -*- coding: utf-8 -*-

list = map(int, raw_input().split())
a = list[0]
b = list[1]

if a < b:
    print "a < b"
elif a > b:
    print "a > b"
else:
    print "a == b"