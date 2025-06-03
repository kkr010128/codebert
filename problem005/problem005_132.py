import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    c = a * b
    while b:
        a, b = b, a % b
    print(str(a) + ' ' + str(c / a))