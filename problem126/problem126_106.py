#!/usr/bin/env python3


def solve(xs: "List[int]"):
    for idx, x in zip(range(1, 6), xs):
        if x == 0:
            return idx


def main():
    x = list(map(int, input().split()))
    answer = solve(x)
    print(answer)


if __name__ == "__main__":
    main()
