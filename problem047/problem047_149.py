from sys import stdin
 
while True:
    (a, op, b) = stdin.readline().split(' ')
    a = int(a)
    b = int(b)
    if op == "?":
        break;
    elif op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a // b)