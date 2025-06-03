#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B = map(int, readlines())
    list = [1, 2, 3]
    list.remove(A)
    list.remove(B)
    print(list[0])


if __name__ == '__main__':
    main()
