#!/usr/bin/env python3


def solve(S: int, W: int):
    if W >= S:
        return "unsafe"
    return "safe"


def main():
    S, W = map(int, input().split())
    answer = solve(S, W)
    print(answer)


if __name__ == "__main__":
    main()
