# -*- coding: utf-8 -*-
fibs = {0: 1, 1: 1}


def fib(n):
    if n not in fibs:
        fibs[n] = fib(n - 1) + fib(n - 2)

    return fibs[n]


if __name__ == '__main__':
    n = int(input())
    print(fib(n))

