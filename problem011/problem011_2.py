def main():
    X, Y = map(int, input().split())

    print(gcd(X, Y))

def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        a = b
        b = r
        return gcd(a, b)

main()