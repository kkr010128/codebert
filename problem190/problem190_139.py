#!/usr/bin/python3
import sys
input = lambda: sys.stdin.readline().strip()
def pal(s, L, R):
    return s[L] == s[R] and (L >= R or pal(s, L + 1, R - 1))

s = input()
n = len(s)
print('Yes' if pal(s, 0, n - 1) and pal(s, 0, (n - 1) // 2 - 1) and pal(s, (n + 3) // 2 - 1, n - 1) else 'No')