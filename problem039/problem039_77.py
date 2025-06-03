def isIncremental(a, b, c):
    """
    a: int
    b: int
    c: int

    returns "Yes" if a < b < c, otherwise "No"

    >>> isIncremental(1, 3, 8)
    'Yes'
    >>> isIncremental(3, 8, 1)
    'No'
    >>> isIncremental(1, 1, 1)
    'No'
    """
    if a >= b:
        return "No"
    elif b >= c:
        return "No"
    else:
        return "Yes"

if __name__ == '__main__':
#   import doctest
#   doctest.testmod()

    ival = input().split(' ')
    print(isIncremental(int(ival[0]), int(ival[1]), int(ival[2])))