import sys


def a_c(f):
    s = f.read().decode().strip()
    return 'ABC' if s == 'ARC' else 'ARC'


def main():
    ans = a_c(sys.stdin.buffer)
    print(ans)


if __name__ == '__main__':
    main()