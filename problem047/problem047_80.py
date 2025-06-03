import sys

for v in iter(sys.stdin.readline,""):
    a,op,b = v.split()
    a = int(a)
    b = int(b)
    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(a/b)
    elif op == '?':
        break