#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def update(x):
    y = x * 105 // 100
    r = y % 1000
    y = y // 1000 * 1000
    if r: y += 1000
    return y

def main():
    n = int(input())

    x = 100000
    for _ in range(n):
        x = update(x)

    print(x)

if __name__ == "__main__": main()