def lcm(x, y):
    return x / gcd(x, y) * y

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b);

a, b = [int(i) for i in input().split()]
print(int(lcm(a, b)))