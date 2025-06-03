import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    from math import gcd
    a,b=MI()
    print((a*b)//gcd(a,b))
    

main()
