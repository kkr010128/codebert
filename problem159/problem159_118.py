#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    X = int(input())

    y = 100
    ans = 0
    while y < X:
        ans += 1
        y += y // 100
    print(ans)

if __name__ == '__main__':
    main()
