#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(s: str):
    if s[2] == s[3] and s[4] == s[5]:
        print(YES)
    else:
        print(NO)
    return


def main():
    s = sys.stdin.readline().strip()  # type: str
    solve(s)


if __name__ == '__main__':
    main()
