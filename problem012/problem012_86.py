#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def isprime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        else:
            return True


def main():
    n = int(input())
    ms = (int(input()) for i in range(n))
    print(len(list(filter(isprime, ms))))

if __name__ == "__main__":
    main()