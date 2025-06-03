#!/usr/bin/env python3


def main():
    a, b, c = map(int, input().split())
    k = int(input())

    for i in range(k):
        if a < b < c:
            break
        elif a >= b:
            b *= 2
        elif b >= c:
            c *= 2

    if a < b < c:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
