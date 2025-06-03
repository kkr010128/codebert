import sys

for stdin in sys.stdin:
    inlist = stdin.split()

    a = int(inlist[0])
    b = int(inlist[2])
    op = inlist[1]
    
    if op == "?":
        break
    elif op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "/":
        print(a // b)
    elif op == "*":
        print(a * b)