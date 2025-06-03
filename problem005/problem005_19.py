def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

def lcm(a, m):
    return a * b / gcd(a, b);

while True:
    try:
        a, b = map(int, raw_input().split())
        print gcd(a, b), lcm(a, b)
    except (EOFError):
        break