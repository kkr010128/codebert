# -*- coding: utf-8 -*-
import functools


@functools.lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    n = int(input())
    print(fib(n))

