import sys
read = sys.stdin.read
readlines = sys.stdin.readlines

def main():
    a, b, c, d = map(int, input().split())
    while a > 0 and c > 0:
        c -= b
        if c <= 0:
            print('Yes')
            sys.exit()
        a -= d
        if a <= 0:
            print('No')
            sys.exit()


if __name__ == '__main__':
    main()
