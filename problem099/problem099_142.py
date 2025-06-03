# Binary Search

def isOK(i, key):
    '''
    問題に応じて返り値を設定
    '''
    cnt = 0
    for v in a:
        cnt += (v + i - 1) // i - 1

    return cnt <= key


def binary_search(key):
    '''
    条件を満たす最小/最大のindexを求める
    O(logN)
    '''
    ok = 10 ** 9  # 条件を満たすindexの上限値/下限値
    ng = 0        # 条件を満たさないindexの下限値-1/上限値+1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2

        if isOK(mid, key):  # midが条件を満たすか否か
            ok = mid
        else:
            ng = mid
    
    return ok


n, k = map(int, input().split())
a = list(map(int, input().split()))
 
print(binary_search(k))