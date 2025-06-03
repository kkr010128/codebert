cont = True

while cont:
    data = input().split(" ")
    a = int(data[0])
    b = int(data[2])
    op = data[1]
    if op == "?":
        cont = False
    elif op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    else:
        print(int(a/b))