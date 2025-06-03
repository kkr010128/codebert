# -*- coding: utf-8 -*-

while True:
    x, y = map(int, raw_input().split())
    if x+y:
        if x < y:
            print "%d %d" %(x, y)
        else:
            print "%d %d" %(y, x)
    else:
        break;