while True:
    inputs = input().split(' ')
    a = int(inputs[0])
    op = inputs[1]
    b = int(inputs[2])
    if op == "?":
        break
    elif op == "+":  # (和)
        print(a + b)
    elif op == "-":  # (差)
        print(a - b)
    elif op == "*":  #(積)
        print(a * b)
    else:  # "/"(商)
        print(a // b)
