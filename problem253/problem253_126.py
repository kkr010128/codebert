#!/usr/bin python3
# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())
    if abs(A-B)%2==0:
        ret = abs(A-B)//2
    else:
        A, B = min(A, B), max(A, B)
        ret = min(B-(B-A+1)//2, N-(B-A-1)//2-A)
    print(ret)

if __name__ == '__main__':
    main()