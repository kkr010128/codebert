while True:
    x = input()
    if x == '0 0':break
    print(*sorted(map(int,x.split())))
