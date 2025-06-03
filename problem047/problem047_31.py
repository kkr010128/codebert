import sys

s = sys.stdin.readlines()
for i in s:
    a, op, b = i.split()
    a, b = int(a), int(b)
    if op == '?':
        break
    elif op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a // b)