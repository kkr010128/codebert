def ri():
    return int(input())


def rii():
    return [int(v) for v in input().split()]


def solve(x):
    return 0 if x else 1


if __name__ == "__main__":
    print(solve(ri()))