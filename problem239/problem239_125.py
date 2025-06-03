#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    C = readline().rstrip().decode()
    print(chr(ord(C) + 1))


if __name__ == '__main__':
    main()
