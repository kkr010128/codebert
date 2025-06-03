#!/usr/bin/env python3
def main():
    import sys

    input = sys.stdin.readline

    N, K = map(int, input().split())
    res = [False for _ in range(N)]
    for _ in range(K):
        _ = int(input())
        A = [int(x) for x in input().split()]
        for i in A:
            res[i - 1] = True
    print(res.count(False))



if __name__ == '__main__':
    main()
