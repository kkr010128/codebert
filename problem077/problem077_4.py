# coding:UTF-8
import sys

if __name__ == '__main__':
    # ------ 入力 ------#
    # 1行入力
    # a = int(input())    # 数字
    # a = input()     # 文字列
    aList = list(map(int, input().split()))     # スペース区切り連続数字
    # a = input().split()     # スペース区切り連続文字列
    # a = [int(c) for c in input()]   # 数字→単数字リスト変換

    # 定数行入力
    x = 5
    # a = [int(input()) for _ in range(x)] # 数字
    # a = [input() for _ in range(x)] # 文字
    # a = [list(map(int, input().split())) for _ in range(x)]     # スペース区切り連続数字(行列)
    # a = [input().split() for _ in range(x)]     # スペース区切り連続文字
    # a = [[int(c) for c in input()] for _ in range(x)]  # 数字→単数字リスト変換(行列)

    # スペース区切り連続 数字、文字列複合
    # a = []
    # for _ in range(x):
    #     aa, bb = input().split()
    #     a.append((int(aa), bb))

    # ------ 処理 ------#
    a = aList[0]
    b = aList[1]
    c = aList[2]
    d = aList[3]
    m = max(a*c, a*d, b*c, b*d)

    # ------ 出力 ------#
    print("{}".format(m))
