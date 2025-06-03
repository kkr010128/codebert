# Date [ 2020-08-29 21:59:01 ]
# Problem [ e.py ]
# Author Koki_tkg
# After Contest

import sys
import math
# import bisect
# import numpy as np
# from decimal import Decimal
# from numba import njit, i8, u1, b1 #JIT compiler
# from itertools import combinations, product
# from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846

def read_str():      return sys.stdin.readline().strip()
def read_int():      return int(sys.stdin.readline().strip())
def read_ints():     return map(int, sys.stdin.readline().strip().split())
def read_ints2(x):   return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a%b==0 else GCD(b, a%b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)

# osa_k 法 O(NloglogN + logA)
class PrimeFactorization():
    def __init__(self, num):
        self.num = num
        self.factor_table = [0] * (num + 1)
        self.eratosthenes()

    def eratosthenes(self):
        for i in range(2, self.num + 1):
            if self.factor_table[i] == 0:
                self.factor_table[i] = i
                for j in range(i * i, self.num + 1, i):
                    if self.factor_table[j] == 0:
                        self.factor_table[j] = i
    
    def factorization(self, a):
        now = a
        ret = []
        while now > 1:
            cnt = 0
            prime = self.factor_table[now]
            while now % prime == 0:
                cnt += 1
                now //= prime
            ret.append((prime, cnt))
        return ret

def Main():
    n = read_int()
    a = read_int_list()
    max_num = max(a)

    pf = PrimeFactorization(max_num + 1)
    used_prime = [False] * (max_num + 1)
    for x in a:
        factor = pf.factorization(x)
        for prime, cnt in factor:
            if used_prime[prime]:
                break
            used_prime[prime] = True
        else:
            continue
        break
    else:
        print('pairwise coprime')
        exit()

    gcd_num = a[0]
    for x in a[1:]:
        gcd_num = math.gcd(gcd_num, x)
    print('setwise coprime' if gcd_num == 1 else 'not coprime')

if __name__ == '__main__':
    Main()