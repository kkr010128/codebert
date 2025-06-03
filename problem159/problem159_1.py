#!/usr/bin/env python3
def main():
    import sys

    input = sys.stdin.readline

    X = int(input())

    cnt = 0
    res = 100
    while True:
        if res >= X:
            print(cnt)
            break
        res += res // 100
        cnt += 1


if __name__ == '__main__':
    main()
