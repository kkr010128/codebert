def distance(x, y, p):
    """returns Minkowski's distance of vactor x and y if p > 0.
    if p == 0, returns Chebyshev distance

    >>> d = distance([1, 2, 3], [2, 0, 4], 1)
    >>> print('{:.6f}'.format(d))
    4.000000
    >>> d = distance([1, 2, 3], [2, 0, 4], 2)
    >>> print('{:.6f}'.format(d))
    2.449490
    >>> d = distance([1, 2, 3], [2, 0, 4], 3)
    >>> print('{:.6f}'.format(d))
    2.154435
    >>> d = distance([1, 2, 3], [2, 0, 4], 0)
    >>> print('{:.6f}'.format(d))
    2.000000
    """
    if p == 0:
        return max([abs(a-b) for (a, b) in zip(x, y)])
    else:
        return sum([abs(a-b) ** p for (a, b) in zip(x, y)]) ** (1/p)


def run():
    dim = int(input())  # flake8: noqa

    x = [int(i) for i in input().split()]
    y = [int(j) for j in input().split()]

    print(distance(x, y, 1))
    print(distance(x, y, 2))
    print(distance(x, y, 3))
    print(distance(x, y, 0))


if __name__ == '__main__':
    run()
