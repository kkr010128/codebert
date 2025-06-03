while True:
    i = input().split()
    result = 0
    if i[1] == '+':
        result = int(i[0]) + int(i[2])
    elif i[1] == '-':
        result = int(i[0]) - int(i[2])
    elif i[1] == '*':
        result = int(i[0]) * int(i[2])
    elif i[1] == '/':
        result = int(i[0]) // int(i[2])
    elif i[1] == '?':
        break

    print(result)