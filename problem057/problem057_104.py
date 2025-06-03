while True:
    ( m, f, r) = [ int(i) for i in input().split()]
    if ( m == f == r == -1): break

    total = m + f
    achieve = ''
    if m == -1 or f == -1 or total < 30: achieve = 'F'
    elif total < 50 and r < 50: achieve = 'D'
    elif total < 65: achieve = 'C'
    elif total < 80: achieve = 'B'
    else: achieve = 'A'

    print(achieve)