import fractions

if __name__ == '__main__':
    x, y = [int(_) for _ in input().split()]
    print(fractions.gcd(x, y))