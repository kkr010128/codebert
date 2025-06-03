import sys


def main():
    input = sys.stdin.buffer.readline
    l = int(input())
    print((l / 3) ** 3)


if __name__ == "__main__":
    main()
