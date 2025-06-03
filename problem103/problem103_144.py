#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1000

    for i in range(1, N):
        if A[i - 1] < A[i]:
            stock = ans // A[i - 1]
            ans += stock * (A[i] - A[i - 1])
    print(ans)


if __name__ == "__main__":
    main()
