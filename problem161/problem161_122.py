import sys
import math


def solve(a: int, b: int, n: int) -> int:
    x = min(n, b - 1)
    return math.floor(a * ((x / b) - int(x / b)))


def main():
    input = sys.stdin.buffer.readline
    a, b, n = map(int, input().split())
    print(solve(a, b, n))


if __name__ == '__main__':
    main()
