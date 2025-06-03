import sys

for s in sys.stdin:
    a = list(map(int, s.split()))
    b = a[0]
    c = a[1]

    while c != 0:
        b, c = c, b%c

    d = a[0] * a[1] / b
    print(int(b), int(d))