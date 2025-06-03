def print_chessboard(h, w):
    """
    h: int
    w: int
    outputs chessboard using '#' and '.'

    >>> print_chessboard(3, 4)
    #.#.
    .#.#
    #.#.
    >>> print_chessboard(5, 6)
    #.#.#.
    .#.#.#
    #.#.#.
    .#.#.#
    #.#.#.
    >>> print_chessboard(2, 2)
    #.
    .#
    """
    for i in range(h):
        line = ''
        for j in range(w):
            if (i+j) % 2 == 0:
                line += '#'
            else:
                line += '.'
        print(line)


if __name__ == '__main__':

    while True:
        (h, w) = [int(i) for i in input().split(' ')]
        if h == 0 and w == 0:
            break
        print_chessboard(h, w)
        print()