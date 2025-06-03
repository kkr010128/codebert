#!/usr/bin/env python3

def main():
    K, X = map(int, open(0).read().split())
    if (500 * K >= X):
        print('Yes')
    else:
        print('No')


main()