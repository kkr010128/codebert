a, b = list(map(int, input().split(' ')))
def gcd(l, r):
    return l if r == 0 else gcd(r, l % r)
print(int(a * b / gcd(a, b)))