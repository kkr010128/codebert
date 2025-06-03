while True:
    ( a, op, b) = input().split()
    a = int(a)
    b = int(b)

    if op == '?':
        break
    elif op == '+':
        print( '{0}'.format( a + b))
    elif op == '-':
        print( '{0}'.format( a - b))
    elif op == '*':
        print( '{0}'.format( a * b))
    elif op == '/':
        print( '{0}'.format( a // b))