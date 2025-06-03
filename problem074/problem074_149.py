# coding:UTF-8
import sys
from math import factorial

MOD = 998244353
INF = 10000000000

def main():
    n, k = list(map(int, input().split()))  # スペース区切り連続数字
    lrList = [list(map(int, input().split())) for _ in range(k)]  # スペース区切り連続数字(行列)

    s = []
    for l, r in lrList:
        for i in range(l, r+1):
            s.append(i)
    s.sort()

    sum = [0] * (n + 1)
    Interm = [0] * (2 * n + 1)
    sum[1] = 1
    for i in range(1, n):
        for j in range(k):
            l, r = lrList[j][0], lrList[j][1]
            Interm[i+l] += sum[i]
            Interm[i+r+1] -= sum[i]
        sum[i+1] = (sum[i] + Interm[i+1]) % MOD

    # result = Interm[n]
    result = (sum[n] - sum[n-1]) % MOD
    # ------ 出力 ------#
    print("{}".format(result))

if __name__ == '__main__':
    main()
