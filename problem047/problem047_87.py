import math
while True:
    ins = input().split()
    x = int(ins[0])
    op = ins[1]
    y = int(ins[2])
    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    elif op == "/":
        print(math.floor(x / y))
    elif op == "*":
        print(x * y)
    elif op == "?":
        break
    else:
        break