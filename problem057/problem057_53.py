while True:
    m, f, r = map(int, raw_input().split())
    p = ""
    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1:
        p = "F"
    else:
        s = m + f
        if s >= 80:
            p = "A"
        elif s >= 65:
            p = "B"
        elif s >= 50:
            p = "C"
        elif s >= 30:
            p = "C" if r >= 50 else "D"
        else:
            p = "F"
    print(p)