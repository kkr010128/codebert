def mondai(W, H, x, y, r):
    if (x - r < 0 or
        x + r > W or
        y - r < 0 or
        y + r > H):
        print('No')
    else:
        print('Yes')

W, H, x, y, r = [int(x) for x in input().split()]
mondai(W, H, x, y, r)