# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque

def run():
    N = input()
    S = input()
    dp = [0] * 1000
    ans = 0
    for n in S:
        n = int(n)
        #print(dp)
        for i in range(1000):
            if i // 100 == n and dp[i] == 0:
                dp[i] = 1
                #print(f'{i} -> 1')
            elif (i // 10) % 10 == n and dp[i] == 1:
                dp[i] = 2
                #print(f'{i} -> 2')
            elif i % 10 == n and dp[i] == 2:
                dp[i] = 3
                #print(f'{i} -> 3')
                ans += 1
    print(ans)

    #print(factorials)
if __name__ == "__main__":
    run()