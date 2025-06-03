while(True):
    x, y = map(int, input().split())
    if(x == y == 0):
        break
    if(x <= y):
        print("%d %d" % (x, y))
    else:
        print("%d %d" % (y, x))