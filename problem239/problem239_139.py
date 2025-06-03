#!/usr/bin/env python3


def solve(C: str):
    return chr(ord(C) + 1)


def main():
    C = input().strip()
    answer = solve(C)
    print(answer)


if __name__ == "__main__":
    main()
