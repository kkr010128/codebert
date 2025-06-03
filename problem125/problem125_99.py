import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

X = int(input())
from math import gcd
print(360*X//gcd(360, X)//X)