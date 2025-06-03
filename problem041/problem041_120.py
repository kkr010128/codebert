(w, h, x, y, r) = input().rstrip().split(' ')
w = int(w)
h = int(h)
x = int(x)
y = int(y)
r = int(r)

if 0 + r <= x <= w - r and 0 + r <= y <= h - r:
    print('Yes')
else:
    print('No')