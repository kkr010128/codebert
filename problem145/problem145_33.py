#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    (N, M) = map(int, input().split())
    neighbor = [[] for _ in range(N+1)]
    for _ in range(M):
        (A,B) = map(int, input().split())
        neighbor[A] += B,
        neighbor[B] += A,

    guide = [0 for _ in range(N+1)]

    # 1の部屋から幅優先で道しるべを置く
    
    # 探索候補
    target = [1]
    checked = [1]
    while len(target) > 0:
        # 候補の先頭から取る
        n = target.pop(0)
        # nから伸びる行き先
        dests = neighbor[n]
        # すでに道しるべがあるものは除く
        dests = filter(lambda d: guide[d] == 0, dests)
        # 道しるべを置く
        for d in dests:
            guide[d] = n
            checked += d,
            # 探索候補の末尾に追加
            target += d,

    print('Yes')
    for i in range(2,N+1):
        print(guide[i])

main()
