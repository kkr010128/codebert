while True:
    s = input().split()
    a = int(s[0])
    op = s[1]
    b = int(s[2])
    if op == "?":
        break
    
    if op == "+":
        print(a+b)
    if op == "-":
        print(a-b)
    if op == "*":
        print(a*b)
    if op == "/":
        print(a//b)
