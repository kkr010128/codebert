from collections import Counter, defaultdict, deque
import bisect
from sys import stdin, stdout
from itertools import repeat
import math
import random

# sys.stdin = open('input')

def inp():
    re = map(int, raw_input().split())
    if len(re) == 1:
        return re[0]
    return re

def inst():
    return raw_input().strip()

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def my_main():
        n, k, c = inp()
        st = inst()
        front, end = [], []
        def get(now, ans):
            while now < n:
                if len(ans) == k:
                    return
                for i in range(now, n):
                    if st[i]=='o':
                        ans.append(i+1)
                        now = i+c+1
                        break
                else:
                    break
        get(0, front)
        st = st[::-1]
        get(0, end)
        for i in range(len(end)):
            end[i] = n-end[i]+1
        end.sort()
        if len(front)!=k or len(end)!=k:
            return
        ans = []
        # print front, end
        for i in range(k):
            if front[i] == end[i]:
                ans.append(front[i])
        if ans:
            print '\n'.join(map(str, ans))

my_main()
