#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    As = map(int, readline().split())
    if sum(As) >= 22:
        print('bust')
    else:
        print('win')


if __name__ == '__main__':
    main()
