def gcd(a, b):
    while True:
        a, b = b, a%b
        if b == 0:
            return a

def lcm(a, b):
    return int((a*b) // gcd(a, b))

a, b = map(int, input().split())

print(lcm(a, b))