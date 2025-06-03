# -*- coding: utf-8 -*-

def cube(x):
    """
    return x cubed

    >>> cube(2)
    8

    >>> cube(3)
    27

    >>> cube(10)
    1000

    """

    return x**3


if __name__ == '__main__':
    x = int(raw_input())
    print cube(x)