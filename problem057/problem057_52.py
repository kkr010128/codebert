while True:
    m, f, r = map(int, input().split())
    if m == -1 and f== -1 and r == -1:
        break
    mf = m + f
    if  m == -1 or f == -1 or mf < 30:
       print('F')
    elif mf < 50:
        if r < 50:
            print('D')
        else:
            print('C')
    elif mf < 65:
        print('C')
    elif mf < 80:
        print('B')
    else:
        print('A')