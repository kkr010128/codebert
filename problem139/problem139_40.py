import sys
input = sys.stdin.readline

# from collections import deque

def linput(_t=int):
    return list(map(_t, input().split()))

def gcd(n,m):
    while m: n,m = m, n%m
    return n

def lcm(n,m): return n*m//gcd(n,m)

def main():
    # N = int(input())
    # vA = [int(input()) for _ in [0,]*N]
    h,m,H,M,K = linput()

    res = 60*H + M - 60*h - m - K

    print(res)
    # print(("No","Yes")[res%2])
    # print(*vR, sep="\n")

main()
