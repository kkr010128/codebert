W, H, x, y, r = map(int, input().split())

if (2*r <= (x+r) <= W) & (2*r <= (y+r) <= H):
    print('Yes')
else:
    print('No')

