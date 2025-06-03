# coding: utf-8
while 1:
    a, op, b = input().split()
    if op == "+":
        ans = int(a) + int(b)
    elif op == "-":
        ans = int(a) - int(b)
    elif op == "*":
        ans = int(a) * int(b)
    elif op == "/":
        ans = int(a) // int(b)
    else:
        break
    print(ans)