#!/usr/bin/env python3
# atcoder 
# Türkler var mı?
# Herkese memnün oldum
import sys

iimr = lambda: map(int, sys.stdin.readline().rstrip().split())



def 関数(a, v, b, w, t):
    
    d = abs(a - b)
    if v <= w:
        return "NO"
    s = v-w
    if d <= s*t:
        return "YES"
    else:
        return "NO" 

def çözmek():
    A, V = map(int, input().split())
    B, W = map(int, input().split())
    T = int(input())

    res = []
    res.append(関数(A, V, B, W, T))
    print(*res, sep="\n")

if __name__ == "__main__":
    çözmek()
