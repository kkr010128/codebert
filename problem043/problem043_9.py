while 1:
    x, y = [int(i) for i in input().split()]
    if x < y:
        print((x), (y))
    elif y < x:
        print((y), (x))
    elif x == 0 and y == 0:
        break
    else:
        print((x),(y))