# coding=utf-8


def fib(number):
    if number == 0 or number == 1:
        return 1
    memo1 = 1
    memo2 = 1

    for i in range(number-1):
        memo1, memo2 = memo1+memo2, memo1
    return memo1


if __name__ == '__main__':
    N = int(input())
    print(fib(N))

