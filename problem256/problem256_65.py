import fractions
a, b = map(int, input().split())

def lcm(a,b):
    return (a*b)//fractions.gcd(a,b)

print(lcm(a,b))