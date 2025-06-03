# coding: utf-8

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())

print(int(gcd(n, m)))