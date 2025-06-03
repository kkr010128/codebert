while True:
    m, f, r = map(int, (input().split()))
    score = m + f
    if m == f == r == -1:
        break
    else:
        if m == -1 or f == -1:
            print("F")
        elif score >= 80:
            print("A")
        elif 80 > score >= 65:
            print("B")
        elif 65 > score >= 50:
            print("C")
        elif 50 > score >= 30 and r >= 50:
            print("C")
        elif 50 > score >= 30 and r < 50:
            print("D")
        else:
            print("F")