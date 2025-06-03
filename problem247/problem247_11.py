import math
#import numpy as np
import queue
from collections import deque,defaultdict
import fractions
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

#2で何回割れるかを数える関数
def t_per2(k):
    return format(k,'b')[::-1].find('1')

def main():
    n,m = map(int,ipt().split())
    a = [int(i) for i in ipt().split()]
    k2 = t_per2(a[0])
    l = a[0]//2
    for ai in a[1::]:
        if not k2 == t_per2(ai):
            print(0)
            exit()
        l = l*(ai//2)//(fractions.gcd(l,ai//2))
        if l > m:
            print(0)
            exit()
    print((m+l)//(2*l))
    return

if __name__ == '__main__':
    main()
