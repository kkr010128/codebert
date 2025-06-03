while True:
    c = input().split()
    x, y = int(c[0]), int(c[1])
    if x == y == 0:
        break
    if y < x:
        x, y = y, x
    print("%d %d" % (x, y))

