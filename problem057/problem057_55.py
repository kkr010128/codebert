import sys

for i in sys.stdin:
    scores = list(map(int, i.split()))
    m = scores[0]
    f = scores[1]
    r = scores[2]
    if m == f == r == -1:
        break
    elif (m == -1) or (f == -1):
        print("F")
    elif m + f >= 80:
        print("A")
    elif 65 <= (m + f) < 80:
        print("B")
    elif 50 <= (m + f) < 65:
        print("C")
    elif 30 <= (m + f) < 50:
        if r >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")