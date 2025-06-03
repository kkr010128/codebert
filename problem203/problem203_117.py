import sys


def solve(a, b):
    for i in range(1, 10000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            return i
    return -1


def main():
    input = sys.stdin.buffer.readline
    a, b = map(int, input().split())
    print(solve(a, b))


if __name__ == "__main__":
    main()
