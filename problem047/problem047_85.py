while True:
    a, op, b = raw_input().split()
    if op == "?":
        break
    else:
        if op == '+':
            print int(a) + int(b)
        elif op == '-':
            print int(a) - int(b)
        elif op == '*':
            print int(a) * int(b)
        elif op == '/':
            print int(a) / int(b)
        else:
            print "error"