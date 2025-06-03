#!/usr/bin python3
# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

def main():
    a, b, c = map(int, input().split())
    x = ((c-a-b)**2-4*a*b > 0 ) and (c > a+b)
    print('NYoe s'[x::2])

if __name__ == '__main__':
    main()