def grade(m, f, r):
    if m == -1 or f == -1:
        return 'F'
    s = m + f
    if s >= 80:
        return 'A'
    elif s >= 65:
        return 'B'
    elif s >= 50:
        return 'C'
    elif s < 30:
        return 'F'
    elif r >= 50:
        return 'C'
    else:
        return 'D'


while True:
    m, f, r = map(int, input().split())
    if m == f == r == -1:
        break
    print(grade(m, f, r))