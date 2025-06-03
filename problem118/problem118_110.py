import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()



def main():
    n = I()
    ans = 0
    N = 10**7 + 1
    prime = [True] * N
    prime[1] = False
    n_yaku = [1] * N
    min_prime = [1] * N

    for i in range(2, N):
        if not prime[i]:
            continue
        n_yaku[i] = 2
        min_prime[i] = i
        num = i + i
        while num < N:
            min_prime[num] = i
            prime[num] = False
            num += i
    for i in range(2, N):
        if prime[i]:
            continue
        j = i
        cnt = 0
        while j % min_prime[i] == 0:
            # print('j: ', j)
            # print('prime: ', min_prime[i])
            j //= min_prime[i]
            cnt += 1
        n_yaku[i] = n_yaku[j] * (cnt + 1)
    ans = 0
    for i in range(1, n+1):
        ans += i * n_yaku[i]
    print(ans)


main()

