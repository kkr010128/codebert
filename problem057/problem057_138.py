def give_grade(m, f, r):
    if m == -1 or f == -1:
        return "F"
    elif m + f < 30:
        return "F"
    elif m + f < 50:
        return "D" if r < 50 else "C"
    elif m + f < 65:
        return "C"
    elif m + f < 80:
        return "B"
    else:
        return "A"

while True:
    m, f, r = map(int, input().split())
    if m == f == r == -1:
        break
    else:
        print(give_grade(m, f, r))