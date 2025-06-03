#!/usr/bin/env python3
def main():
    N, K = map(int, input().split())
    H = sorted([int(x) for x in input().split()])

    if K == 0:
        print(sum(H))
    elif N > K:
        print(sum(H[:-K]))
    else:
        print(0)


if __name__ == '__main__':
    main()
