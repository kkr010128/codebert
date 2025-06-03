while True:
    a, op, b = input().split()
    if op == '?':
        break
    if op == '/':
        op = '//'
    print(eval(a + op + b))