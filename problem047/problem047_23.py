while True:
    l = input().split()

    if l[1] == '?':
        break
    print(int(eval(l[0]+l[1]+l[2])))