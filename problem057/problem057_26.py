while True:
    m, f, r = (int(x) for x in input().split())
    if (m, f, r) == (-1, -1, -1):
        break
    sum_score = m + f

    if m == -1 or f == -1:
        print("F")
    elif sum_score >= 80:
        print("A")
    elif 65 <= sum_score < 80:
        print("B")
    elif 50 <= sum_score < 65:
        print("C")
    elif 30 <= sum_score < 50:
        print("C") if r >= 50 else print("D")
    else:
        print("F")