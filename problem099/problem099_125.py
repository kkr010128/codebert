#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = list(map(int, input().split()))

ng = 0
ok = 10 ** 9

# able(X) を、すべての丸太を X 以下の長さに切れる場合 1 , そうでない場合 0 を返す関数とする
# 二分探索によって、able(X) が 1 に切り替わる X 点を見つける


def able(x):
    count = 0
    for i in range(N):
        if A[i] % x:
            count += A[i] // x
        else:
            count += A[i] // x - 1

    if count <= K:
        return True
    else:
        return False


while ok - ng > 1:
    mid = ng + (ok - ng) // 2
    if able(mid):
        ok = mid
    else:
        ng = mid

print(ok)
