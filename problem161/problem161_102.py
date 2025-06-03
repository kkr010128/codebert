a, b, n = map(int, input().split())


def calc(x):
    return int(a * x / b) - a * int(x / b)


if n < b:
    print(calc(n))
else:
    print(calc(b-1))