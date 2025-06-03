W, H, x, y, r = map(int, input().split(' '))
# 高さ
if (r <= y <= (H - r)) and (r <= x <= (W - r)):
    print('Yes')
else:
    print('No')
