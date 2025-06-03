#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N - K):
        print("Yes" if A[i] < A[i + K] else "No")


if __name__ == "__main__":
    main()
