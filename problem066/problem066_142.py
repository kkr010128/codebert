while True:
    Str = list(input())
    if Str[0] == '-':
        break
    m = int(input())
    for i1 in range(m):
        h = int(input())
        for i2 in range(h):
            Str.extend(Str[0])
            Str.remove(Str[0])
    for i in range(len(Str)):
        print(Str[i], end = '')
    print()