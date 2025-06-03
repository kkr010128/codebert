def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    X = int(input())
    ans = 360 // gcd(X, 360)
    print(ans)


if __name__ == "__main__":
    main()
