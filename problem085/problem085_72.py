# coding:UTF-8
import sys
from math import factorial

MOD = 10 ** 9 + 7
INF = 10000000000

# 素数列挙
def primeNumList(n):
    d = [d for d in range(0, n+1)]
    if n < 2:
        return [[],d]
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
            d[j] = i
    return [[i for i in range(n + 1) if is_prime[i]], d]

def main():
    # ------ 入力 ------#
    n = int(input())    # 数字
    aList = list(map(int, input().split()))     # スペース区切り連続数字

    # ------ 処理 ------#
    amax = max(aList)
    pl = primeNumList(amax)
    countList = [0] * (amax+1)

    if pl[0] != []:
        for a in aList:
            at = a
            sl = []
            while at != 1:
                s = pl[1][at]
                sl.append(s)
                at = int(at / s)
            sl2 = list(set(sl))
            for s in sl2:
                countList[s] += 1
        m = max(countList)
    else:
        m = 0

    # ------ 出力 ------#
    if m == len(aList):
        print("not coprime")
    elif m >= 2:
        print("setwise coprime")
    else:
        print("pairwise coprime")


if __name__ == '__main__':
    main()
