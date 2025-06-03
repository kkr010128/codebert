import fractions

while True:
    try:
        (a, b) = map(int, raw_input().split())
        c = fractions.gcd(a, b)
        print c, ((a*b)/c)
    except EOFError:
        break