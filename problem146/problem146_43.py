#!/usr/bin/env python3
from sys import stdin
from collections import defaultdict
from math import gcd

def II(): return int(input())
def MII(): return map(int, input().split())
def LII(): return list(map(int, input().split()))

def main():
    MOD = 1000000007
    
    N, *AB = map(int, stdin.buffer.read().split())
    d = defaultdict(int)
    zeros = 0
    for a, b in zip(AB[::2], AB[1::2]):
        if a == 0 and b == 0:
            zeros += 1
        else:
            g = gcd(a, b)
            a //= g
            b //= g
            if a < 0:
                a *= -1
                b *= -1
            if a == 0 and b == -1:
                b = 1
            d[(a, b)] += 1
        
    ans = 1
    free = 0
    for (a, b), n in d.items():
        if b > 0:
            if (b, -a) in d:
                m = d[(b, -a)]
                ans = ans * (pow(2, n, MOD) + pow(2, m, MOD) - 1) % MOD
            else:
                free += n
        else:
            if (-b, a) not in d:
                free += n

    ans = (ans * pow(2, free, MOD) + zeros - 1) % MOD
    print(ans)

if __name__ == '__main__':
    main()
