def count_divisors(num, start, end):
    """
    num: positive int
    start: positive int
    end: positive int(end > start)
    returns numbers of devisors of i between start and end

    >>> count_divisors(80, 5, 14)
    3
    >>> count_divisors(12, 1, 4)
    4
    """
    count = 0
    for i in range(start, end+1):
        if num % i == 0:
            count += 1

    return count

if __name__ == '__main__':
    #import doctest
    #doctest.testmod()

    (a, b, c) = [int(i) for i in input().split(' ')]

    print(count_divisors(c, a, b))