while(True):
    t = input()
    if t == '-':
        break
    for i in range(int(input())):
        num = int(input())
        t = t[num:] + t[:num]
    print(t)
