import math


def distance(p1, p2):
    """returns the distance between p1 and p2

    >>> d = distance((0, 0), (1, 1))
    >>> print("{0:.5f}".format(d))
    1.41421
    """
    (x1, y1) = p1
    (x2, y2) = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def run():
    x1, y1, x2, y2 = [float(i) for i in input().split()]

    print(distance((x1, y1), (x2, y2)))


if __name__ == '__main__':
    run()

