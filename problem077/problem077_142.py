a, b, c, d = map(int, input().split())

if b < 0:
    if c <= 0:
        print(a * c)
    else:
        print(b * c)

elif a <= 0:
    if d < 0:
        print(a*c)
    elif a <= 0:
        print(max(a*c, b*d))
    else:
        print(b*d)

else:
    if d < 0:
        print(a * d)
    else:
        print(b * d)