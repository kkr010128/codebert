# import string
import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    from itertools import accumulate


    B = [0] + A
    B = list(accumulate(B))  # 累積和を格納したリスト作成

    # この問題は長さが1-Nの連続部分の和の最大値を出せというものなので以下の通り

    S=B[-1]
    minans = 10 ** 20
    for i in range(1,N):
        val=abs(B[i]-(S-B[i]))
        minans=min(minans,val)
    print(minans)


resolve()