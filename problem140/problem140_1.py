#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    t = input()
    bef = '!'
    s = ""
    for c in t:
        nc = c
        if c == '?':
            nc = "D"
        bef = nc
        s += nc
    print(s)



if __name__ == '__main__':
    main()
