from math import gcd
def main():
    a, b = map(int, input().split())
    r = (a * b) // gcd(a, b)
    print(r)

if __name__ == '__main__':
    main()