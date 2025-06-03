# coding:UTF-8
import sys


def resultSur97(x):
    return x % (1000000000 + 7)


if __name__ == '__main__':
    # ------ 入力 ------#
    # 1行入力
    n = int(input())    # 数字
    # a = input()     # 文字列
    # aList = list(map(int, input().split()))     # スペース区切り連続数字
    # aList = input().split()     # スペース区切り連続文字列
    # aList = [int(c) for c in input()]   # 数字→単数字リスト変換

    # 定数行入力
    x = n
    # aList = [int(input()) for _ in range(x)] # 数字
    # aList = [input() for _ in range(x)] # 文字
    aList = [list(map(int, input().split())) for _ in range(x)]     # スペース区切り連続数字(行列)
    # aList = [input().split() for _ in range(x)]     # スペース区切り連続文字
    # aList = [[int(c) for c in input()] for _ in range(x)]   # 数字→単数字リスト変換(行列)

    # スペース区切り連続 数字、文字列複合
    # aList = []
    # for _ in range(x):
    #     aa, bb = input().split()
    #     a.append((int(aa), bb))

    # ------ 処理 ------#
    zmin = aList[0][0] + aList[0][1]
    zmax = aList[0][0] + aList[0][1]
    wmin = aList[0][0] - aList[0][1]
    wmax = aList[0][0] - aList[0][1]

    for i in range(len(aList)):
        x = aList[i][0]
        y = aList[i][1]

        z = x + y
        w = x - y

        if z < zmin:
            zmin = z
        if z > zmax:
            zmax = z
        if w < wmin:
            wmin = w
        if w > wmax:
            wmax = w

    disMax = max(zmax-zmin, wmax-wmin)
    # ------ 出力 ------#
    print("{}".format(disMax))
    # if flg == 0:
    #     print("YES")
    # else:
    #     print("NO")
