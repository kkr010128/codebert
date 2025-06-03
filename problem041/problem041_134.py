values = input()
W, H, x, y, r = [int(x) for x in values.split()]
flag = True

if x - r < 0 or x + r > W:
    flag = False
if y - r < 0 or y + r > H:
    flag = False

if flag:
    print('Yes')
else:
    print('No')