import sys

for i in sys.stdin.readlines():
    m, f, r = [int(x) for x in i.split()]
    if m == f == r == -1:
        break
    elif (m == -1 or f == -1) or (m + f < 30):
        print('F')
    elif m + f >= 80:
        print('A')
    elif m + f >= 65:
        print('B')
    elif m + f >= 50 or (30 <= m + f <= 50 and r >= 50):
        print('C')
    elif m + f >= 30:
        print('D')