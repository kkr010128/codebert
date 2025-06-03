while True:
    a, op, b = [x for x in input().split()]
    a, b = int(a), int(b)
    if op == "?":
        break
    elif op == "+":
        c = a + b
    elif op == "-":
        c = a - b
    elif op == "*":
        c = a * b
    else:
        c = a // b
    print(c)