def main():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    for answer in calc(n, x, y):
        print("{:.6f}".format(answer))


def calc(n, x, y):
    ret = []
    patterns = [1, 2, 3]
    for pattern in patterns:
        sum = 0
        for i in range(0, n):
            sum += (abs(x[i] - y[i])) ** pattern
        ret.append(sum ** (1 / pattern))

    last = 0
    for i in range(0, n):
        last = max(last, abs(x[i] - y[i]))
    ret.append(last)

    return ret


if __name__ == "__main__":
    main()

