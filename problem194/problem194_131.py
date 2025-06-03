#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    H, W = map(int,input().split())
    sth, stw = 0, 0
    glh, glw = H-1, W-1

    INF = 10000
    Gmap = [list(input()) for _ in range(H)]
    Dist = [[INF]*W for _ in range(H)]
    direc = {(1,0), (0,1)}

    if Gmap[0][0]=='#':
        Dist[0][0]=1
    else:
        Dist[0][0]=0

    for h in range(H):
        for w in range(W):
            nw = Gmap[h][w]
            for d in direc:
                hs, ws = h + d[0], w + d[1]
                if 0<=hs<H and 0<=ws<W:
                    cr = Gmap[hs][ws]
                    Dist[hs][ws] = min(Dist[hs][ws], Dist[h][w] + (cr=='#' and nw=='.'))
    print(Dist[glh][glw])

if __name__ == '__main__':
    main()