#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    S = readline().rstrip().decode()
    print('x' * len(S))


if __name__ == '__main__':
    main()
