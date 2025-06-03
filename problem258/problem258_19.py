import sys
read = sys.stdin.read
def main():
    n = int(input())
    if n <= 9 or n % 2 == 1:
        print(0)
        sys.exit()

    n5 = 5
    r = 0
    while n >= n5 * 2:
        r += n // (n5 * 2)
        n5 *= 5
    print(r)

if __name__ == '__main__':
    main()