from sys import stdin

def score(mid, fin, re):
    if mid == -1 or fin == -1:
        return "F"
    elif (mid+fin) >= 80:
        return "A"
    elif (mid+fin) >= 65:
        return "B"
    elif (mid+fin) >= 50:
        return "C"
    elif (mid+fin) >= 30:
        if re >= 50:
            return "C"
        else:
            return "D"
    else:
        return "F"

while True:
    m, f, r = [int(x) for x in stdin.readline().rstrip().split()]
    if m == -1 and f == -1 and r == -1:
        break
    else:
        print(score(m, f, r))
