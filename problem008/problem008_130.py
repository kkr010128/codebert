# -*- coding: utf-8 -*-
'''
所要時間は、分位であった。
'''


# ライブラリのインポート
#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
import collections
#import math
global time, Ls, Lf, E,LG,c,n
time = 1

def main():
    global time, Ls, Lf, E, LG,c,n
    c = 0
    n = int(input().strip())
    E = [[] for _ in range(n)]
    LG = collections.deque()
    for line in sys.stdin:
        Ltmp = list(map(int, list(line.strip().split())))
        if not Ltmp[1] == 0: 
            E[Ltmp[0]-1] = Ltmp[2:]
    Ls = [0]*n 
    Lf = [0]*n
    dfs(0)
    for i in range(n):
        print(i+1, Ls[i],Lf[i])
    
def dfs(cur):
    global time, Ls, Lf, E, LG,c,n
    LG.append(cur)
    if Ls[cur] == 0: Ls[cur] = time
    time += 1
    for i in range(len(E[cur])):
        check = E[cur][i] - 1
        if Ls[check] == 0: dfs(check)
    if Lf[cur] == 0:
        Lf[cur] = time
    try:
        x = LG.pop()
        if x == cur: x = LG.pop() 
        dfs(x)
    except:
        time += 1
        for i in range(c,n):
            if Ls[i] == 0:
                c = i
                dfs(i) 
    return




    


    
if __name__ == '__main__':
    main()

