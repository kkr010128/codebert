import sys
from collections import deque

input = sys.stdin.readline


def dfs(N):
    alphabet = "abcdefghij"
    stack = deque(["a"])
    while stack:
        s = stack.pop()
        if len(s) == N:
            print(s)
            continue
        suffixes = []
        for al in alphabet:
            suffixes.append(al)
            if al not in s:
                break
        for suffix in reversed(suffixes):
            stack.append("".join((s, suffix)))


def main():
    N = int(input())

    dfs(N)


if __name__ == "__main__":
    main()
