x, y = (int(a) for a in input().split())
foot = 0
y_tmp = y
y_tmp2 = y

for i in range(x):
    y_tmp -= 2 * i + 4 * (x - i)
    y_tmp2 -= 4 * i + 2 * (x - i)
    if y_tmp == 0 or y_tmp2 == 0:
        print('Yes')
        exit()
    else:
        y_tmp = y
        y_tmp2 = y

print('No')