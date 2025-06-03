# -*- coding: utf-8 -*-
import sys

def main():
    H,W,K = list(map(int, sys.stdin.readline().split()))
    C_list = [list( sys.stdin.readline().rstrip() ) for _ in range(H)]

    bit_H = 1 << H
    bit_W = 1 << W
    cnt_K = 0

    for b_H in range(bit_H):
        for b_W in range(bit_W):
            cnt_black = 0

            for row in range(H):
                for col in range(W):
                    if (C_list[row][col] == "#") and ( b_H & (1 << row) ) and ( b_W & (1 << col) ):
                        cnt_black += 1
            
            if cnt_black == K:
                cnt_K += 1
    
    print(cnt_K)


if __name__ == "__main__":
    main()
