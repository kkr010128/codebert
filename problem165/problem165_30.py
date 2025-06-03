#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    S = {'0'}
    for i in range(N):
        S.add(input())
    print(len(S) - 1)

if __name__ == '__main__':
    main()
