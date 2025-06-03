while True:
    a = input()
    b = a.split(' ')
    H = int(b[0])
    W = int(b[1])
    if H == 0 and W ==0:
        break
    for i in range(H):
        c = '#'*W
        print(c)
    print()