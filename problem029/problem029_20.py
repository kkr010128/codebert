x1, y1, x2, y2 = map(float, raw_input().split())
num = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
if num == 0:
    print 0
else:
    xi = num
    for _ in range(100):
        xi = (xi + (num / xi)) / 2.0
    print xi