'''
研究室PCでの解答
'''
import math
#import numpy as np
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7

def main():
    x,y = map(int,ipt().split())

    #nCrをmodで割った余りを求める。Nに最大値を入れて使用。
    N = 7*10**5
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル
    def cmb(n,r,mod=(10**9+7)):
        if r<0 or r>n :
            return 0
        r = min(r,n-r)
        return g1[n]*g2[r]*g2[n-r]%mod
    for i in range(2,N+1):
        g1.append((g1[-1]*i)%mod)
        inverse.append((-inverse[mod % i]*(mod//i))%mod)
        g2.append((g2[-1]*inverse[-1])%mod)


    if (2*x-y)%3 == 0 and 2*x-y >= 0 and (2*y-x)%3 == 0 and 2*y-x >= 0:
        print(cmb((x+y)//3,(2*x-y)//3))
    else:
        print(0)



    return None

if __name__ == '__main__':
    main()
