import sys

def gcd(a,b):
    while a % b != 0:
        a, b = b, a % b
    return b

def lcm(a,b,g):
    _a = a // g
    _b = b // g
    return _a * _b * g

def run():
    data = []
    for n in sys.stdin:
        a, b = list(map(int, n.split()))
        data.append((a,b))

    for _data in data:
        a, b = _data
        g = gcd(a,b)
        l = lcm(a,b,g)
        print(g, l)

if __name__ == '__main__':
    run()


