MAXN = 45
fibs = [-1] * MAXN


def fib(n):
    """Returns n-th fibonacci number

    >>> fib(3)
    3
    >>> fib(10)
    89
    >>> fib(20)
    10946
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif fibs[n] == -1: 
        fibs[n] = fib(n-1) + fib(n-2)

    return fibs[n]


def run():
    n = int(input())
    print(fib(n))


if __name__ == '__main__':
    run()

