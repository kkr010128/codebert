#!/usr/bin/env python3


def solve(S: str):
    return sum([a != b for a, b in zip(S, reversed(S))]) // 2


def main():
    S = input().strip()
    answer = solve(S)
    print(answer)


if __name__ == "__main__":
    main()
