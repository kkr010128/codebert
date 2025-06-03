import sys

i=1
for line in sys.stdin:
    a=int(line)
    if a == 0:
        break
    else:
        print 'Case {0}: {1}'.format(i, a)
        i+=1