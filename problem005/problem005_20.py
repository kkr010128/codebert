import math

while True:
    try:
        a, b = list(map(int, input().split()))
        print('{0} {1}'.format(math.gcd(a, b), int(a * b / math.gcd(a, b))))
    except EOFError:
        break

