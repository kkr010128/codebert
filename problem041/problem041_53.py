x = input().split()
W, H, x, y, r = int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4])

if r <= x and r <= y and x + r <= W and y + r <= H:
    print('Yes')
else:
    print('No')
