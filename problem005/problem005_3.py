
def gcd(a,b):
    while a%b :
        a,b=b,a%b
    return b
def lcm(a,b):
    return a*b/gcd(a,b)

while True :
    try:
        a,b = map(int,raw_input().split())
        a,b = max(a,b), min(a,b)
        print "%d" % gcd(a,b),
        print "%d" % lcm(a,b)
    except EOFError:
        break