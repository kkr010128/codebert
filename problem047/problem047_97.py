while 1:
    a, b, c = raw_input().split()
    if b == "?":
        break
    a = int(a)
    c = int(c)
    if b == "+":
        print a+c
    elif b == "-":
        print a-c
    elif b == "*":
        print a*c
    elif b == "/":
        print a//c
