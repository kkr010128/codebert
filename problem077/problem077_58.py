a,b,c,d = map(int, input().split())
if a >=0:
    if c > 0:
        print(b * d)
    elif d < 0:
        print(a * d)
    else:
        print(b*d)

elif a < 0 and b >= 0:
    if c >= 0:
        print(b * d)
    elif d <= 0:
        print(a * c)
    else:
        ac = a * c
        bd = b * d
        if ac >= bd:
            print(ac)
        else:
            print(bd)
else:
    if c >= 0:
        print(b * c)
    elif d <= 0:
        print(a * c)
    else:
        print(a * c)