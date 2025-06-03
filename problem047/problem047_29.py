a = []
while True:
    b = raw_input().split()
    if b[1] == '?':
        break
    c = [int(b[0]), b[1], int(b[2])]
    a.append(c)
for list in a:
    x, op, y = list
    if op == '+':
        print x + y
    elif op == '-':
        print x - y
    elif op == '*':
        print x * y
    else:
        print x / y