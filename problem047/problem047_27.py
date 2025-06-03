while  True:
    inputs = input().split()
    a = int(inputs[0])
    op = inputs[1]
    b = int(inputs[2])

    if op == "?":
        break

    result = 0
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = int(a / b)
    print(result)