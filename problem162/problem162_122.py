#!/usr/bin/env python3
import sys

def main():
    N, M = map(int, input().split())
    
    if M % 2 == 1:
        for i in range(M//2):
            print(i+1,M-i)
        for j in range(M//2 + 1):
            print(M+1+j,2*M+1-j)
    else:
        for i in range(M//2):
            print(i+1, M+1-i)
        for j in range(M//2):
            print(M+2+j,2*M+1-j)

if __name__ == '__main__':
    main()