# Aizu - 0005
def De(a):
    res = []
    tmp = 2
    while a != 1:
        while not (a % tmp):
            a = round(a / tmp)
            res.append(tmp)
        tmp += 1
    return res

while True:
    try:
        tmp = input()
        a = [int(i) for i in tmp.split(' ')]
    except:
        break
    b = De(a[1])
    a = De(a[0])
    pa, pb = 0, 0
    GCD, LCM = 1, 1
    while True:
        if pa == len(a):
            for i in range(pb, len(b)):
                LCM *= b[i]
            break;
        if pb == len(b):
            for i in range(pa, len(a)):
                LCM *= a[i]
            break;
        if a[pa] == b[pb]:
            GCD *= a[pa]
            LCM *= a[pa]
            pa += 1
            pb += 1
            continue
        if a[pa] < b[pb]:
            LCM *= a[pa]
            pa += 1
            continue
        if a[pa] > b[pb]:
            LCM *= b[pb]
            pb += 1
            continue
    print('%d %d'%(GCD, LCM))