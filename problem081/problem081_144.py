#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    d, t, s = map(int, input().split())
    if d / s <= t:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
