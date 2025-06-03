while True:
    m, f, r = map(int, input().split())
    score = m + f
    if m == f == r == -1:
        break
    elif m == -1 or f == -1:
        print('F')
    elif score >= 80:
        print('A')
    elif score >= 65:
        print('B')
    elif score >= 50 or (score >= 30 and r >= 50):
        print('C')
    elif score >= 30:
        print('D')
    else:
        print('F')

