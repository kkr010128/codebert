# -*- coding: utf-8 -*-
from sys import stdin
input = stdin.readline
MOD = 10**9+7

def main():
    D, T, S = list(map(int,input().split()))
    print('Yes' if D/S <= T else 'No')

if __name__ == "__main__":
    main()
