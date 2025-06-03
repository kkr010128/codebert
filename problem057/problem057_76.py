while True:
    m, t, f = map( int, raw_input().split())
    if m == -1 and t == -1 and f == -1:
        break
    if m == -1 or t == -1:
        r = "F"
    elif (m + t) >= 80:
        r = "A"
    elif (m + t) >= 65:
        r = "B"
    elif (m + t) >= 50:
        r = "C"
    elif (m + t) >= 30:
        if f >= 50:
            r = "C"
        else:
            r = "D"
    else:
        r = "F"

    print r