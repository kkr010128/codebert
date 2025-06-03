
def printComparison(a, b): 
    """ 
    a: int
    b: int
    outputs the comparison result of a and b

    >>> printComparison(1, 2)
    a < b
    >>> printComparison(4, 3)
    a > b
    >>> printComparison(5, 5)
    a == b
    >>> printComparison(-20, -10)
    a < b
    """
    operator = ''
    if a > b:
        operator = '>' 
    elif a < b:
        operator = '<' 
    else:
        operator = '=='

    print('a', operator, 'b')


if __name__ == '__main__':
    ival = input().split(' ')
    printComparison(int(ival[0]), int(ival[1]))