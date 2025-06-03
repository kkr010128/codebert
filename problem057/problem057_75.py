while True:
    mid, term, add = map(int, input().split())
    if mid == -1 and term == -1 and add == -1:
        break
    if mid == -1 or term == -1:
        rank = 'F'
    elif mid + term >= 80:
        rank = 'A'
    elif mid + term >= 65:
        rank = 'B'
    elif mid + term >= 50:
        rank = 'C'
    elif mid + term >= 30:
        if add >= 50:
            rank = 'C'
        else:
            rank = 'D'
    else:
        rank = 'F'
    print(rank)