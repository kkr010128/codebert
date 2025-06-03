# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
from itertools import product, accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque

def run():
    A,B = map(int, sysread().split())
    K = math.gcd(A,B)
    factorials = []
    L = int(max(A,B)**0.5)
    for i in range(2, L+1):
        done = False
        limit = int(i ** 0.5)
        for j in factorials:
            if j > limit:break
            if not i % j:
                done = True
                break
        if not done:
            factorials.append(i)

    factors = [1]
    for f in factorials:
        if f > K:break
        if not K % f:
            factors.append(f)
            while not K % f:
                K = K // f

    if K != 1:
        factors.append(K)
    print(len(factors))


    #print(factorials)
if __name__ == "__main__":
    run()