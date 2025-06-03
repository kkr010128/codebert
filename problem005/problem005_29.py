def gcd(a, b):
    return gcd(b, a%b) if b else a
    
while True:
    try:
        a, b = map(int, raw_input().split())
        ans = gcd(a, b)
        print ans, a*b//ans
    except EOFError:
        break