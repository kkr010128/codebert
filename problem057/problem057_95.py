while True:
    m,f,r = [int(x) for x in input().split()]
    if (m,f,r)==(-1,-1,-1): break
    s_mf = m + f
    if   m < 0 or f < 0: mark = 'F'
    elif s_mf <  30:     mark = 'F'
    elif s_mf >= 80:     mark = 'A'
    elif s_mf >= 65:     mark = 'B'
    elif s_mf >= 50:     mark = 'C'
    elif r    >= 50:     mark = 'C'
    else:                mark = 'D'
    print(mark)