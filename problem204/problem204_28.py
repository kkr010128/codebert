import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
eps = 1.0e-20
MOD = 10**9+7

def lcm(x,y):
    return x*y//gcd(x,y)
def mint():
    return map(int,input().split())
def lint():
    return list(map(int,input().split()))
def ilint():
    return int(input()), list(map(int,input().split()))
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)
def ston(c, c0='a'):
    return ord(c)-ord(c0)
def ntos(x, c0='a'):
    return chr(x+ord(c0))
class counter(dict):
    def __init__(self, *args):
        super().__init__(args)
    def add(self,x):
        self.setdefault(x,0)
        self[x] += 1

S = input()
L = deque()
for i in range(len(S)):
    L.append(S[i])
Q = int(input())
rev = False
for _ in range(Q):
    q = input()
    if q[0]=='1':
        rev = not rev
    else:
        _,f,c = q.split()
        if rev==(f=='1'):
            L.append(c)
        else:
            L.appendleft(c)
L = list(L)
if rev:
    L = L[::-1]
print(''.join(L))