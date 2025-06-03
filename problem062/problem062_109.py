while True:
    a = input()
    if a == '0':
        break
    print(sum(map(int,*a.split())))