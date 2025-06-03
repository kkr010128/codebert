#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    mod = 10**9+7
    N = int(input())
    A = list(map(int, input().split()))
    C = [0] * 3
    ret = 1
    for i in range(N):
        ret *= C.count(A[i])
        ret %= mod
        for j in range(3):
            if C[j]==A[i]:
                C[j]+=1
                break
    print(ret)

if __name__ == '__main__':
    main()