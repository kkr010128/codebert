# -*- coding: utf-8 -*-
from sys import stdin
input = stdin.readline
MOD = 10**9+7

def main():
    n = int(input().strip())
    buf = 9**n
    ans = 10**n - buf - buf + 8**n
    print(ans%MOD)

if __name__ == "__main__":
    main()
