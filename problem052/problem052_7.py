#!/usr/bin/env python

import sys

def main():
    n = int(raw_input())
    for i in range(3, n+1):
        if three(i):
            sys.stdout.write(' {}'.format(i))
    print

def three(i):
    if i%3 == 0:
        return True

    while i > 0:
        if i%10 == 3:
            return True
        i /= 10

    return False

if __name__ == '__main__':
    main()

