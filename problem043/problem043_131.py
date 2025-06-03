import sys
while True:
    (x, y) = [int(i) for i in sys.stdin.readline().split()]
    if x == 0 and y == 0:
        break
    if x > y:
        x, y = y, x
    print("%d %d" % (x, y))