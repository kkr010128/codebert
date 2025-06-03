def main():
    a, b = map(int, input().split())
    import math

    print(int(a*b/math.gcd(a,b)))
    


if __name__ == "__main__":
    main()
