from math import gcd


def main():
    a, b = map(int, input().split())

    ans = a * b // gcd(a, b)

    print(ans)


if __name__ == "__main__":
    main()
