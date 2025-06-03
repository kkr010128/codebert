def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

X = int(input())
print(lcm(360, X)//X)