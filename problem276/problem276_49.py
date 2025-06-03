import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    A = input_int_list()
    A_sum = sum(A)
    cusum = [0] * (n + 1)
    ans = float("inf")
    for i in range(1, n + 1):
        cusum[i] = cusum[i - 1] + A[i - 1]
        ans = min(ans, abs(cusum[i] - (A_sum - cusum[i])))
    print(ans)

    return


if __name__ == "__main__":
    main()
