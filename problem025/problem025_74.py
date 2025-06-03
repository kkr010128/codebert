# coding: utf-8
N = int(input())
A = [int(i) for i in input().split()]
q = int(input())
m = [int(i) for i in input().split()]
MAX_LENGTH = len(A)
dp = [[-1 for i in range(max(m) + 1)] for j in range(MAX_LENGTH + 1)]
# i番目以降の値を使ってmを作ればTrueを返す
def fullSearch(i, m):
    # 終了条件
    if m < 0:
        return False
    elif dp[i][m] != -1:
        return dp[i][m]
    elif m == 0:
        return True
    elif i >= MAX_LENGTH:
        return False
    else:
        # 全探索かっこわるい
        res = fullSearch(i + 1, m) or fullSearch(i + 1, m - A[i])
    # のでメモ化
    dp[i][m] = res
    return res
for mi in m:
    print("yes" if fullSearch(0, mi) else "no")