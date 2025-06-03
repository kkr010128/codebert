#!/usr/bin/env python3
def main():
    N, M = map(int, input().split())
    A = [int(x) for x in input().split()]

    if N >= sum(A):
        print(N - sum(A))
    else:
        print(-1)


if __name__ == '__main__':
    main()
