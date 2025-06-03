import sys
input = sys.stdin.readline
from collections import *

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def factorize(n):
    fct = []
    
    for i in range(2, int(n**0.5)+1):
        c = 0
        
        while n%i==0:
            n //= i
            c += 1
            
        if c>0:
            fct.append((i, c))
    
    if n>1:
        fct.append((n, 1))
    
    return fct

A, B = map(int, input().split())
fct = factorize(gcd(A, B))
ans = 1+len(fct)
print(ans)