"""
最小公倍数LCMを求めて、LCMを各Aで除した商を合計すればよい
"""
from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
def main():
    mod = 10**9 +7
    N = int(input())
    A = list(map(int,input().split()))
    l = A[0]
    for i in range(1,N):
        l = lcm(l,A[i])

    ans = 0
    for a in A:
        ans += l//a
    print(ans%mod)
main()