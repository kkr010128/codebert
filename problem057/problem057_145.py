
while True:
    m,f,r = map(int,raw_input().split())

    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1:
        print('F')
    elif m+ f >= 80:
        print('A')
    elif m + f >= 65 and m + f < 80:
        print('B')
    elif m + f >= 50 and m + f < 65 or r >= 50:
        print('C')
    elif m + f >= 30 and m + f < 50:
        print('D')
    elif m + f <= 29:
        print('F')