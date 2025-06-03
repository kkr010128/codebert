# -*- coding: utf-8 -*-

memo = ['' for i in xrange(45)]


def recursion(n):
    if n == 0 or n == 1:
        return 1

    return recursion(n - 1) + recursion(n - 2)


def memo_search(n):
    if memo[n] != '':
        return memo[n]
    else:
        if n == 0 or n == 1:
            memo[n] = 1
            return 1
        memo[n] = memo_search(n - 1) + memo_search(n - 2)
        return memo[n]

if __name__ == '__main__':
    n = input()
    # print recursion(n)
    print memo_search(n)