from sys import exit
import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n = ii()
s,t = input().split()

for i in range(len(s)):
    print(s[i] + t[i] ,end = "")