def print_rectangle(h, w):
    """
    h: int
    w: int
    outputs rectangle using '#'

    >>> print_rectangle(3, 4)
    ####
    ####
    ####
    >>> print_rectangle(5, 6)
    ######
    ######
    ######
    ######
    ######
    >>> print_rectangle(2, 2)
    ##
    ##
    """
    for i in range(h):
        print('#' * w)


if __name__ == '__main__':
    #import doctest
    #doctest.testmod()

    while True:
        (h, w) = [int(i) for i in input().split(' ')]
        if h == 0 and w == 0:
            break
        print_rectangle(h, w)
        print()