#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(A: int, B: int, C: int, D: int):
    while True:
        # 高橋
        C -= B
        if C <= 0:
            return YES
        # 青木
        A -= D
        if A <= 0:
            return NO


def main():
    A, B, C, D = map(int, input().split())
    answer = solve(A, B, C, D)
    print(answer)


if __name__ == "__main__":
    main()
