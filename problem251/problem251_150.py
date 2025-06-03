# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, k = [int(x) for x in input().split()]
    R, S, P = [int(x) for x in input().split()]
    s = input()
    ans = 0
    b = []
    for i in range(n):
        e = s[i]
        if i < k or s[i] != s[i-k] or s[i-k] == b[i-k]:
            if e == 'r':
                ans += P
                b.append('p')
            elif e == 'p':
                ans += S
                b.append('s')
            elif e == 's':
                ans += R
                b.append('r')
        else:
            b.append(e)
    print(ans)
    
    

        
    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

R s
S p
P r

"""
