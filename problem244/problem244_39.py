#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    K, X = map(int, readline().split())
    if 500 * K >= X:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
