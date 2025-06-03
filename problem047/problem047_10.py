while True:
    Input = raw_input().split()

    a  = int(Input[0])
    op = Input[1]
    b  = int(Input[2])

    if   op == "+":
        ans = a + b
        print ans
    elif op == "-":
        ans = a - b
        print ans
    elif op == "/":
        ans = a / b
        print ans
    elif op == "*":
        ans = a * b
        print ans
    elif op == "?":
        break