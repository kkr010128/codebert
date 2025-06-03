#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B = map(int, readline().split())
    print(max(A - 2 * B, 0))


if __name__ == '__main__':
    main()
