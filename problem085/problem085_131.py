import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
def prime_factorize(n):
    prime_fact = []
    while n%2 == 0:
        prime_fact.append(2)
        n//=2
    f = 3
    while f * f <= n:
        if n % f == 0:
            prime_fact.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime_fact.append(n)
    return prime_fact

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    prefix_gcd = a[0]
    dp = [0]*(max(a)+1)
    for i in range(n):
        prefix_gcd = math.gcd(prefix_gcd,a[i])

    for i in range(n):
        d = prime_factorize(a[i])
        d = set(d)
        for j in d:
            dp[j]+=1
    pair = True
    for i in range(len(dp)):
        if dp[i] > 1:
            pair = False
    if pair == True and prefix_gcd == 1:
        print("pairwise coprime")
    elif pair == False and prefix_gcd == 1:
        print("setwise coprime")
    else:
        print("not coprime")