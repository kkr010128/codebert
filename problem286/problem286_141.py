#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B = map(int, readline().split())
    if (A <= 9) & (B <= 9):
        print(A * B)
    else:
        print(-1)


if __name__ == '__main__':
    main()
