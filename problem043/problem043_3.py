for i in range(3000):
    list = map(int, raw_input().split())
    x = list[0]
    y = list[1]
    if ((x == 0) and (y == 0)):
        break
    else:
        if x <= y:
            print '%d %d'%(x, y)
        else:
            print '%d %d'%(y, x)