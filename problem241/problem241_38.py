import numpy as np
from numba import njit
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

@njit(cache=True)
def pos(W,h,w):
    return h*W+w

def solve(H,W,G):
    N = H*W+W
    INF=10**18

    dp = np.full((N,N),INF)
    for i in range(N):
        dp[i][i] = 0

    for h in range(H):
        for w in range(W):
            if G[h][w]: continue

            for i in range(4):
                dh = [0,1,0,-1][i]
                dw = [1,0,-1,0][i]
                if 0<=h+dh<H and 0<=w+dw<W:
                    if G[h+dh][w+dw]: continue
                    dp[pos(W,h,w)][pos(W,h+dh,w+dw)] = 1
                    dp[pos(W,h+dh,w+dw)][pos(W,h,w)] = 1


    ans = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])


    for i in range(N):
        for j in range(N):
            if dp[i][j] != INF:
                ans = max(ans,dp[i][j])
    

    return ans





def main():
    H,W=mi()
    G = [[0] * W for _ in range(H)]
    for h in range(H):
        S = list(input())
        for w in range(W):
            G[h][w] = S[w] == "#"

    print(solve(H,W,np.array(G,bool)))


def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')

    # basic types: https://numba.pydata.org/numba-doc/0.13/types.html
    cc.export('pos', '(i8,i8,i8,)')(pos)
    cc.export('solve', '(i8,i8,b1[:,:],)')(solve)
    cc.compile()

if __name__ == '__main__':
    try:
        from my_module import solve
        from my_module import pos
    except:
        cc_export()
        exit()

    main()