while True:
    x = input().split()
    if x[1] == '+':
        y = int(x[0])+int(x[2])
        print(y)
    elif x[1] == '-':
        y = int(x[0])-int(x[2])
        print(y)
    elif x[1] == '*':
        y = int(x[0])*int(x[2])
        print(y)
    elif x[1] == '/':
        y = int(x[0])//int(x[2])
        print(y)
    elif x[1] == '?':
        break