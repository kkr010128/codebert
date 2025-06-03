#!/usr/bin/env python3
import sys
import decimal
def input():
    return sys.stdin.readline()[:-1]

def main():
    A, B = map(int, input().split())

    for i in range(1, 10 ** 4):
        a = int(decimal.Decimal(i * 0.08))
        b = int(decimal.Decimal(i * 0.1))
        if a == A and b == B:
            print(i)
            exit()
    print(-1)

if __name__ == '__main__':
    main()
