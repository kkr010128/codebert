while(True):
    num = input()
    if num == '0':
        break
    x = 0
    for i in num:
        x += int(i)
    print(x)
