import sys


def main():
    input = sys.stdin.buffer.readline
    x, y, z = map(int, input().split())
    print(z, x, y)


if __name__ == '__main__':
    main()
