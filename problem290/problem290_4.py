def binary_search(key):
    """二分探索法 O(logN)

    Args:
        key (int): 基準値

    Vars:
        ok (int): 条件を満たすindexの上限値/下限値
        ng (int): 条件を満たさないindexの下限値-1/上限値+1
    
    Returns:
        int: 条件を満たす最小値/最大値
    """
    ok = 10 ** 12
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2

        if isOK(mid, key):
            ok = mid
        else:
            ng = mid
    
    return ok

def isOK(i, key):
    """条件判定

    Args:
        i   (int): 判定対象の値
        key (int): 基準値

    Returns:
        bool: iが条件を満たすか否か
    """
    cnt = 0
    for v, d in l:
        if v > i:
            cnt += (v - i + d - 1) // d

    return cnt <= key


n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

a.sort(reverse=True)
f.sort()
l = []
for i in range(n):
    l.append([a[i]*f[i], f[i]])

print(binary_search(k))