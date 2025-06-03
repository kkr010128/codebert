import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    P = read_ints()
    min_so_far = math.inf
    count = 0
    for p in P:
        min_so_far = min(min_so_far, p)
        if min_so_far >= p:
            count += 1
    return count


if __name__ == '__main__':
    print(solve())
