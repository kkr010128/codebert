#!/usr/bin/env python

def f(x: int) -> int:
    """
    >>> f(0)
    1
    >>> f(1)
    0
    """
    if x == 1:
        return 0
    else:
        return 1


if __name__ == '__main__':
    x = int(input())
    print(f(x))