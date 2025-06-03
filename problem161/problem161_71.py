#!/usr/bin/env python3
def main():
    import sys

    input = sys.stdin.readline

    A, B, N = map(int, input().split())

    x = min(B - 1, N)
    print((A * x) // B - A * (x // B))


if __name__ == '__main__':
    main()
