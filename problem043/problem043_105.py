while 1:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    elif x < y:
        print("%d %d" % (x, y))
    else:
        print("%d %d" % (y, x))