# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque

def sum_count(arr):
    mem = arr[:]
    while True:
        if len(mem) == 1:break
        tmp = []
        while True:
            if len(mem) == 1:
                tmp.append(mem[-1])
                mem = tmp[:]
                break
            if len(mem) == 0:
                mem = tmp[:]
                break
            x1, x2 = mem.pop(), mem.pop()
            tmp.append(int(x1) + int(x2))

    return int(mem[0])

def run():
    N = int(input())
    X = list(input())[::-1]
    lis_bf = []
    lis_af = []
    count1 = sum_count(X)
    sum_val_bf, sum_val_af = 0, 0
    if count1 <= 1:
        for i in range(N):
            tmp_af = 0
            if int(X[i]):
                tmp_af = pow(2, i, count1 + 1)
            lis_af.append(tmp_af)
            sum_val_af += tmp_af
            sum_val_af %= count1 + 1

        for i in list(range(N))[::-1]:
            ans = 0
            if X[i] == '1':
                print(0)
                continue
            else:
                next_val = (sum_val_af + pow(2, i, count1 + 1)) % (count1 + 1)
            # print(next_val)
            ans += 1
            # print(f'i : {i}, next_val : {next_val}')
            while True:
                if next_val == 0: break
                val = next_val
                count_n = sum_count(list(bin(val)[2:]))
                next_val = val % count_n
                ans += 1
                # print(f'next_val : {next_val}')
            print(ans)
        return None

    for i in range(N):
        tmp_bf, tmp_af = 0,0
        if int(X[i]):
            tmp_bf = pow(2, i , count1-1)
            tmp_af = pow(2, i, count1+1)
        lis_bf.append(tmp_bf)
        lis_af.append(tmp_af)
        sum_val_bf += tmp_bf
        sum_val_bf %= count1-1
        sum_val_af += tmp_af
        sum_val_af %= count1 + 1

    for i in list(range(N))[::-1]:
        ans = 0
        if X[i] == '1':
            next_val = (sum_val_bf - lis_bf[i]) % (count1-1)
        else:
            next_val = (sum_val_af + pow(2, i, count1+1)) % (count1+1)
        #print(next_val)
        ans += 1
        #print(f'i : {i}, next_val : {next_val}')
        while True:
            if next_val == 0:break
            val = next_val
            count_n = sum_count(list(bin(val)[2:]))
            next_val = val % count_n
            ans += 1
            #print(f'next_val : {next_val}')
        print(ans)


if __name__ == "__main__":
    run()
