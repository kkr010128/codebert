while(1):
    line = input()
    words = line.split()
    a = int(words[0])
    op = words[1]
    b = int(words[2])
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a // b)
    elif op == '?':
        break