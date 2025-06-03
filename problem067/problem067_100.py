t, h = 0, 0

for i in range(int(input())):
    tc, hc= input().split()
    if tc > hc:
        t += 3
    elif tc < hc:
        h += 3
    else:
        t += 1
        h += 1

print('%d %d' % (t, h))