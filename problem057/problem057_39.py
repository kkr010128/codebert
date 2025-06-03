while(1):
    m, f, r = map(int, input().split())

    if m == -1 and f == -1 and r == -1:
        break

    score = m + f
    if m == -1 or f == -1:
        print("F")
        continue
    if score >= 80:
        print("A")
        continue
    if score >= 65 and score < 80:
        print("B")
        continue
    if score >= 50 and score < 65:
        print("C")
        continue
    if score >= 30 and score < 50:
        if r >= 50:
            print("C")
        else:
            print("D")
        continue
    if score < 30:
        print("F")