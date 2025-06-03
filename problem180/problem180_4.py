INF = int(10e20)


def main():
    N, K = tuple([int(_x) for _x in input().split()])

    minval = N
    sub = N // K - 5
    if sub > 0:
        N = N - K * sub

    for i in range(20):
        N = abs(N - K)
        minval = min(N, minval)

    print(minval)


main()
