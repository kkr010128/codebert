while True:
    data = input().split()
    m = int(data[0])
    f = int(data[1])
    r = int(data[2])
    if m == -1 and f == -1 and r == -1:
        break
    elif m == -1 or f == -1:
        print('F')
    else:
        if m + f >= 80:
            print('A')
        elif m + f >= 65:
            print('B')
        elif m + f >= 50:
            print('C')
        elif m + f >= 30:
            if r >= 50:
                print('C')
            else:
                print('D')
        else:
            print('F')