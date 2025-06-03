def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
def gcd(x, y):
    if(x < y):
        swap(x, y)
    mod = x % y
    if mod == 0:
        return y
    else:
        return gcd(y, mod)
def lcm(x, y):
    return x * y / gcd(x, y)
while True:
    try:
        (a, b) = map(int ,raw_input().split())
    except EOFError:
        break
    print gcd(a, b), lcm(a, b)