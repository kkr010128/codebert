#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    h1, m1, h2, m2, k = rli()
    mins = (h2-h1)*60+m2-m1
    print(mins-k)


if __name__ == '__main__':
    main()
