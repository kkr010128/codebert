#!/usr/bin/env python3
def main():
    import sys

    input = sys.stdin.readline

    X = int(input())

    for a in range(-150, 151):
        for b in range(-150, 151):
            if a ** 5 - b ** 5 == X:
                print(a, b, sep=' ')
                return


if __name__ == '__main__':
    main()
