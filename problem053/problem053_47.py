def reverse(l):
    """
    l: a list
    returns a reversed list

    >>> reverse([1,2,3,4,5])
    [5, 4, 3, 2, 1]
    >>> reverse([3,3,4,4,5,8,7,9])
    [9, 7, 8, 5, 4, 4, 3, 3]
    >>> reverse([])
    []
    """
    length = len(l)
    result = []
    for i in range(length):
        result.append(l[length-i-1])

    return result

if __name__ == '__main__':
    #import doctest
    #doctest.testmod()

    num = int(input())
    ilist = [int(i) for i in input().split(' ')]

    print(' '.join([str(i) for i in reverse(ilist)]))