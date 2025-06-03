#!usr/bin/env python3

import sys


def main():
    while True:
        m, f, r = [int(score) for score in sys.stdin.readline().split()]
        if m == f == r == -1:
            break
        if m == -1 or f == -1:
            print('F')
        elif m+f >= 80:
            print('A')
        elif 80 > m+f >= 65:
            print('B')
        elif 65 > m+f >= 50:
            print('C')
        elif 50 > m+f >= 30:
            if r >= 50:
                print('C')
            else:
                print('D')
        elif m+f < 30:
            print('F')


if __name__ == '__main__':
    main()