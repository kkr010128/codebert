# Date [ 2020-08-23 14:02:31 ]
# Problem [ e.py ]
# Author Koki_tkg
# After Contest

import sys;          from decimal import Decimal
import math;         from numba import njit, i8, u1, b1
import bisect;       from itertools import combinations, product
import numpy as np;  from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846

def read_str():      return sys.stdin.readline().strip()
def read_int():      return int(sys.stdin.readline().strip())
def read_ints(x=0):  return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def lcm(a: int, b: int) -> int: return (a * b) // math.gcd(a, b)

def solve(h,w,bomb):
    row = np.zeros(h, dtype=np.int64)
    column = np.zeros(w, dtype=np.int64)
    
    for y, x in bomb:
        row[y] += 1
        column[x] += 1
        
    max_row = np.max(row)
    max_col = np.max(column)
    val = max_row + max_col

    max_row_lis = np.ravel(np.where(row == row.max()))
    max_col_lis = np.ravel(np.where(column == column.max()))

    for r in max_row_lis:
        for c in max_col_lis:
            if (r, c) not in bomb:
                return val
    
    return val - 1
    

def Main():
    h, w, m = read_ints()
    bomb = set([tuple(read_ints(x=1)) for _ in range(m)])
    
    print(solve(h, w, bomb))


if __name__ == '__main__':
    Main()