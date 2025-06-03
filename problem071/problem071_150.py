# coding:UTF-8
import sys
from math import factorial

MOD = 10 ** 9 + 7
INF = 10000000000


def main():
    # ------ 入力 ------#
    # 1行入力
    a = input()     # 文字列

    # ------ 出力 ------#
    if a[-1] == "s":
        print("{}".format(a + "es"))
    else:
        print("{}".format(a + "s"))

if __name__ == '__main__':
    main()
