while 1:

    x,op,y = raw_input().split()

    if op == "?":
        break

    x = int(x)
    y = int(y)

    if op == "+":
        print x+y
    elif op == "-":
        print x-y
    elif op == "*":
        print x*y
    else:
        print x/y