# coding: utf-8

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def main():
    a, b = map(int, raw_input().split())
    print gcd(a, b)

if __name__ == '__main__':
    main()