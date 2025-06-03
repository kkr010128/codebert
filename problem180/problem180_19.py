#!/usr/bin/env python3
def main():
    N, K = map(int, input().split())

    res = N % K
    print(min(res, abs(res - K)))


if __name__ == '__main__':
    main()
