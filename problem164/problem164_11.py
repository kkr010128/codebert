a, b, c, d = map(int,input().split())
while True:
    c = c - b
    a = a - d
    if c <= 0:
        print('Yes')
        break
    elif a <= 0:
        print('No')
        break
    else:
        pass