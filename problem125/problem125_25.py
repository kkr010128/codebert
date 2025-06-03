def main():
    from math import gcd

    def lcm(a, b):
        return a // gcd(a, b) * b

    x = int(input())
    print(lcm(x, 360) // x)


if __name__ == '__main__':
    main()
