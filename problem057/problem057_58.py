while True:
    m, f, r = map(int, input().split())
    if m == f == r == -1:
        break
    s = m + f
    if m == -1 or f == -1:
        print("F")
    elif s >= 80:
        print("A")
    elif s >= 65:
        print("B")
    elif s >= 50 or r >= 50:
        print("C")
    elif s >= 30:
        print("D")
    else:
        print("F")