#!/usr/bin/env python3


def main():
    x = int(input())
    lank: int = 0
    if 400 <= x <= 599:
        lank = 8
    elif x <= 799:
        lank = 7
    elif x <= 999:
        lank = 6
    elif x <= 1199:
        lank = 5
    elif x <= 1399:
        lank = 4
    elif x <= 1599:
        lank = 3
    elif x <= 1799:
        lank = 2
    else:
        lank = 1
    print(lank)


if __name__ == "__main__":
    main()
