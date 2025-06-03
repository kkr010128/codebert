#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i, a in enumerate(A):
        if (i+1)%2==1 and a%2==1:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()