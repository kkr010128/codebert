while True:
    a, op, b = map(str, input().split(" "))
    if op == "?":
        break
    a, b = int(a), int(b)
    if op == "+":
        c = a + b
    elif op == "-":
        c = a - b
    elif op == "*":
        c = a * b
    else:
        c = a // b
    print(c)
