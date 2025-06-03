import sys
while(True):
    x, y =  map(lambda x: (int, int)[x.isdigit()](x) ,sys.stdin.readline().split(None, 1))
    if x == 0 and y == 0:
        break
    if x < y:
        print("%d %d" % (x, y))
    else:
        print("%d %d" % (y, x))