W, H, x, y, r = [int(temp) for temp in input().split()]

if r <= x <= (W - r) and r <= y <= (H - r) : print('Yes')
else                                       : print('No')