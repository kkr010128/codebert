n = int(input())

num = [-1] * 100


def fibonacci(n):
    if n == 0:
        num[0] = 1
    elif n == 1:
        num[1] = 1

    if num[n] == -1:
        num[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return num[n]


print(fibonacci(n))

