A, B = map(int, input().split())

#最大公約数
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

#最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(A, B))
