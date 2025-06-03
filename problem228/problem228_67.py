#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    H = int(input())

    ans = 0
    n = 1
    for i in range(10**12):
        if H == 1:
            ans += n
            print(ans)
            exit()
        ans += n
        n *= 2
        H = int(H/2)


if __name__ == '__main__':
    main()
