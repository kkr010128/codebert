#!/usr/bin/env python
from fractions import gcd

def main():
    A, B = map(int, input().split())
    print(A * B // gcd(A, B))

if __name__ == '__main__':
    main()