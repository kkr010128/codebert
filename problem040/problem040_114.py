a, b, c = map(int, input().split())
if a > b:
    if b > c:
        print("{} {} {}".format(c, b, a))
    else:
        if a > c:
            print("{} {} {}".format(b, c, a))
        else:
            print("{} {} {}".format(b, a, c))
else:
    if a > c:
        print("{} {} {}".format(c, a, b))
    else:
        if b > c:
            print("{} {} {}".format(a, c, b))
        else:
            print("{} {} {}".format(a, b, c))
    
