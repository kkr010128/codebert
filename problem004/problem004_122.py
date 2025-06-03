# -*- coding: utf-8 -*-

n = int(raw_input())
#print n

while True:
    try:
        a = map(int, raw_input().split())
        #print a
        a.sort(reverse=True)
        #print a

        b, c, d = a
        if (b * b) == ((c * c) + (d * d)):
            print 'YES'
        else:
            print 'NO'
    except EOFError:
        break;