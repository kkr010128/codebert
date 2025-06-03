#!/usr/bin/env python3

def main():
    A, B = map(int, open(0).read().split())
    if (A < 10 and B < 10):
        print(A * B)
    else:
        print('-1')


main()