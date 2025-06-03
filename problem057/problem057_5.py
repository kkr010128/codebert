while True:
    m,f,r = [int(x) for x in input().split()]
    if (m,f,r)==(-1,-1,-1): break
    s_mf = m + f
    if   m < 0 or f < 0: print('F')
    elif s_mf <  30:     print('F')
    elif s_mf >= 80:     print('A')
    elif s_mf >= 65:     print('B')
    elif s_mf >= 50:     print('C')
    elif r    >= 50:     print('C')
    else:                print('D')
