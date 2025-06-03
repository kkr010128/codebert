while 1 :
    a, op, b= raw_input().split()
    c = int(a)
    d = int(b)
    if op == '?': break
    elif op == '+': print c + d
    elif op == '-': print c - d
    elif op == '*': print c * d
    elif op == '/': print c / d