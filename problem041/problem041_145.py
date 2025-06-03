w, h, x, y, r = [int(x) for x in input().split()]
if x + r <= w and x - r >= 0 and y + r <= h and y - r >= 0:
    print('Yes')
else:
    print('No')