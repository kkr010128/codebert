while True:
    ins = input().split()
    
    a = int(ins[0])
    b = int(ins[2])
    op = ins[1]

    if op == "?":
        break
    elif op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "/":
        print(a//b)
    else:
        print(a*b)