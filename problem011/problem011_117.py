# coding:utf-8
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
n = map(int, raw_input().split())
n.sort(reverse=True)
print gcd(n[0],n[1])