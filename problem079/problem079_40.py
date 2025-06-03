# coding:UTF-8
import sys
from math import factorial

def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)

def perm(n, r):
    return factorial(n) // factorial(r)

def resultSur97(x):
    return x % (10**9 + 7)

if __name__ == '__main__':
    # ------ 入力 ------#
    # 1行入力
    s = int(input())    # 数字
    # a = input()     # 文字列
    # aList = list(map(int, input().split()))     # スペース区切り連続数字
    # aList = input().split()     # スペース区切り連続文字列
    # aList = [int(c) for c in input()]   # 数字→単数字リスト変換

    # 定数行入力
    x = 5
    # aList = [int(input()) for _ in range(x)] # 数字
    # aList = [input() for _ in range(x)] # 文字
    # aList = [list(map(int, input().split())) for _ in range(x)]     # スペース区切り連続数字(行列)
    # aList = [input().split() for _ in range(x)]     # スペース区切り連続文字
    # aList = [[int(c) for c in input()] for _ in range(x)]   # 数字→単数字リスト変換(行列)

    # スペース区切り連続 数字、文字列複合
    # aList = []
    # for _ in range(x):
    #     aa, bb = input().split()
    #     a.append((int(aa), bb))

    # ------ 処理 ------#
    a = [1,0,0]
    for i in range(3,s+1):
        sum = 0
        for j in range(i-2):
            sum += a[j]
        a.append(sum)

    out = resultSur97(a[s])
    if s >= 3:
        print(out)
    else:
        print(0)