import sys


def solve(h):
    if h == 1:
        return 1
    else:
        return 1 + 2 * solve(h // 2)


def main():
    input = sys.stdin.buffer.readline
    h = int(input())
    print(solve(h))


if __name__ == "__main__":
    main()
