while True:
    s = raw_input().split()
    a = int(s[0])
    b = int(s[2])
    if s[1] == "?":
        break
    elif s[1] == '+':
        print a + b
    elif s[1] == '-':
        print a - b
    elif s[1] == '*':
        print a * b
    elif s[1] == '/':
        print a / b