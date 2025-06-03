#三井住友2019_F
t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
if (a1 > b1 and a2 > b2) or (a1 < b1 and a2 < b2):
    print(0)
else:
    if a1 < b1 and a2 > b2:
        a1, b1 = b1, a1
        a2, b2 = b2, a2
        
    if t1 * (a1 - b1) > t2 * (b2 - a2):
        print(0)
    elif t1 * (a1 - b1) == t2 * (b2 - a2):
        print('infinity')
    else:
        d = t2 * (b2 - a2) - t1 * (a1 - b1)
        y = t1 * (a1 - b1)
        
        if y % d == 0:
            print(y // d * 2)
        else:
            print(y // d * 2 + 1)