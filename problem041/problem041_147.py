W, H, x, y, r = [int(i) for i in input().split()]
if r <= y <= H - r and r <= x <= W - r:
    print('Yes')
else:
    print('No')