import sys

i = 1

while(1):
    a = raw_input()
    if('0'==a):
        break
    else:
        print "Case %d: %s" % (i, a)
        i += 1