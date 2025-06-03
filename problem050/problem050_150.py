def print_frame(h, w):
    """
    h: int(3 <= h <= 300)
    w: int(3 <= w <= 300)
    outputs a rectangle frame h x w

    >>> print_frame(3, 4)
    ####
    #..#
    ####
    >>> print_frame(5, 6)
    ######
    #....#
    #....#
    #....#
    ######
    >>> print_frame(3, 3)
    ###
    #.#
    ###
    """
    print('#' * w)
    for i in range(h-2):
        print('#' + '.'*(w-2) + '#')
    print('#' * w)


if __name__ == '__main__':

    while True:
        (h, w) = [int(i) for i in input().split(' ')]
        if h == 0 and w == 0:
            break
        print_frame(h, w)
        print()