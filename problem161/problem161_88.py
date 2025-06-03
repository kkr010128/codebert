import sys
import math

def resolve(in_):
    a, b, n = map(int, next(in_).split())
    x = min(b - 1, n)
    return math.floor(a * x / b) - a * math.floor(x / b)


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
