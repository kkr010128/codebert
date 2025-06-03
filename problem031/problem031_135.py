import statistics


def stddev(values):
    """ calculate standard deviation

    >>> s = stddev([70, 80, 100, 90, 20])
    >>> print('{:.5f}'.format(s))
    27.85678
    >>> s = stddev([80, 80, 80])
    >>> print('{:.5f}'.format(s))
    0.00000
    """
    return statistics.pstdev(values)


def run():
    while True:
        c = int(input())  # flake8: noqa
        if c == 0:
            break
        values = [int(i) for i in input().split()]
        print(stddev(values))


if __name__ == '__main__':
    run()
