# coding:UTF-8
import sys
from math import factorial

MOD = 10 ** 9 + 7
INF = 10000000000


def main():
    # ------ 入力 ------#
    n = int(input())    # 数字

    # 定数行入力
    x = n
    dList = [list(map(int, input().split())) for _ in range(x)]     # スペース区切り連続数字(行列)

    # ------ 処理 ------#
    flg = 1
    for i in range(n-2):
        if dList[i][0] == dList[i][1]:
            if dList[i+1][0] == dList[i+1][1]:
                if dList[i+2][0] == dList[i+2][1]:
                    flg = 0

    # ------ 出力 ------#
    if flg == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
