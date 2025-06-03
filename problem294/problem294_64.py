import sys
# sys.setrecursionlimit(100000)
import bisect


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    L = sorted(input_int_list())
    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            idx = bisect.bisect_left(L, L[i] + L[j])
            ans += idx - j - 1
    print(ans)
    return


if __name__ == "__main__":
    main()
