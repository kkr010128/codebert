#!/usr/bin/env python

def solve(A: int, B: int, C: int, K: int):
    if A >= K:
        return K
    K -= A
    if B >= K:
        return A
    K -= B
    return A - K


def main():
    A, B, C, K = map(int, input().split())
    answer = solve(A, B, C, K)
    print(answer)


if __name__ == "__main__":
    main()
