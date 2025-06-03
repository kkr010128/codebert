# -*- coding: utf-8 -*-
loop = 1
while(loop):
    l = list(input().strip().split())
    a = int(l[0])
    b = int(l[2])
    op = l[1]

    if(op == "?"):
        loop = 0
        break;
    elif(op == "+"):
        ret = a + b
    elif(op == "-"):
        ret = a - b
    elif(op == "*"):
        ret = a * b
    elif(op == "/"):
        ret = a / b
    else:
        continue
    print(int(ret))