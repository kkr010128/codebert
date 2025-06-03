def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        r = x % y
        x = y
        y = r

    return x

def main():
    x, y = (int(n) for n in input().split())
    print(gcd(x, y))

main()
