while True:
    a, op, b = raw_input().split()
    if op == '?': break
    a, b = int(a), int(b)
    if op == '+': print a+b
    if op == '-': print a-b
    if op == '*': print a*b
    if op == '/': print a/b