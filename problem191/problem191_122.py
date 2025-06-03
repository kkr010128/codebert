#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    L = int(input())

    print((L/3)**3)

if __name__ == '__main__':
    main()
